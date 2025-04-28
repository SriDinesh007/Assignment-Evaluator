import os
import time
from configs import path_to_REQUIREMENTS_dir

if __name__ == '__main__':
    try:
        requirements = set()
        
        for f in os.listdir(path_to_REQUIREMENTS_dir):
            path_to_f = os.path.join(path_to_REQUIREMENTS_dir,f)
            with open(path_to_f) as f:
                data = f.read()
                data = data.split('\n')
                for requirement in data:
                    requirements.add(requirement.strip())

        with open('requirements.txt','w') as f:
            for requirement in requirements:
                if len(requirement) > 0 :
                    f.write(requirement)
                    f.write('\n')
    
    except Exception as e:
        print(f'An error occured: {e}')
        
