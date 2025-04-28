from configs import path_to_test_cases_file
import json
from master_program import add

if __name__ == '__main__':
    try:
        test_cases = {
            "add" : []
        }

        stop_input = False

        while not stop_input:

            a = int(input('Enter first number to add: '))
            b = int(input('Enter second number to add: '))

            output = add(a,b)

            test_cases["add"].append({'input':[a,b],'output':output})

            stop_input = input('If you want to stop giving input enter "yes" else enter "no": ')

            stop_input = True if stop_input == 'yes' else False

        
        with open(path_to_test_cases_file,'w') as f:
            json.dump(test_cases,f,indent = 2)
            
    except Exception as e:
        print(e)



    