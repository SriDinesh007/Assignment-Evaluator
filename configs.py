import os

# Name of the function we are evaluating
function_name = 'add'

# Path to the test_cases file
test_cases_file_name = 'test_cases.json'
path_to_test_cases_file = os.path.join(os.getcwd(),test_cases_file_name)

# Path to the submissions folder which contains all the student submitted files (.py format)
submissions_folder_name = 'submissions'
path_to_submissions_dir = os.path.join(os.getcwd(),submissions_folder_name)

# Path to REQUIREMENTS folder which contains all the student submitted requirements.txt files 
REQUIREMENTS_folder_name = 'REQUIREMENTS'
path_to_REQUIREMENTS_dir = os.path.join(os.getcwd(),REQUIREMENTS_folder_name)


# Max time that a single test case is allowed
timeout_seconds = 10

# Path to output file which contain the scores of the students after evaluation
# print(os.path.join(os.getcwd(),'evaluated_scores.xlsv'))