import importlib.util
import os
import json
import multiprocessing
from configs import function_name, path_to_test_cases_file, path_to_submissions_dir, timeout_seconds
import pandas as pd

student_scores = {
    'name': [],
    'id': [],
    'score': []
}

def load_student_module(file_path):
    module_name = os.path.splitext(os.path.basename(file_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def run_function_wrapper(task):
    file_path, function_name, args = task
    module = load_student_module(file_path)
    func = getattr(module, function_name)
    return func(*args)

def evaluate_student(absolute_student_file_path, test_input, test_output, id, name):
    tasks = [(absolute_student_file_path, function_name, case) for case in test_input]

    results = []

    with multiprocessing.Pool() as pool:
        async_results = [pool.apply_async(run_function_wrapper, args=(task,)) for task in tasks]
        for async_result in async_results:
            try:
                result = async_result.get(timeout=timeout_seconds)
                results.append(result)
            except multiprocessing.TimeoutError:
                results.append("Time Limit Exceeded")
            except Exception as e:
                results.append(f"Error: {e}")

    # print(results)
    count_correct_answers = sum(1 for i in range(len(results)) if results[i] == test_output[i])
    score = (count_correct_answers / len(test_output)) * 100
    student_scores['id'].append(id)
    student_scores['name'].append(name)
    student_scores['score'].append(round(score,2))

if __name__ == '__main__':
    multiprocessing.freeze_support()  # Important for Windows, safe on Unix
    try:
        with open(path_to_test_cases_file) as f:
            test_cases = json.load(f)
            test_input = [case['input'] for case in test_cases[function_name]]
            test_output = [case['output'] for case in test_cases[function_name]]

        for f in os.listdir(path_to_submissions_dir):
            file = os.path.splitext(f)
            if len(file) > 1:
                file_name, file_extension = file
                if file_extension == '.py':
                    id, first_name, last_name = file_name.split('_')
                    absolute_student_file_path = os.path.abspath(os.path.join(path_to_submissions_dir, f))
                    evaluate_student(absolute_student_file_path, test_input, test_output, id, first_name + ' ' + last_name)

        scores_df = pd.DataFrame(student_scores)

        print(scores_df)
        try:
            with pd.ExcelWriter('evaluated_scores.xlsx') as writer:
                scores_df.to_excel(writer,sheet_name='scores',index=False)
        except Exception as e:
            print(f'An error occured while writing to Excel: {e}')

    except Exception as e:
        print(e)
