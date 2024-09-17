"""
This script will analyze the python code to find os.getenv function calls and extract the environment variables into a .env file.
"""
import re
import sys
from pathlib import Path

if __name__ == '__main__':
    def extract_environ(file_path: str):
        with open(file_path, 'r') as file:
            content = file.read()
            env_vars = re.findall(r'os.getenv\(\"([^\"]*)\"\)', content)
            env_vars = set(env_vars)
            return env_vars


    def write_to_env(env_vars: set):
        with open('../settings/.env', 'w') as file:
            for env_var in env_vars:
                file.write(f'{env_var}=\n')


    if len(sys.argv) < 2:
        print('Usage: python extract_environ.py <file_path>')
        sys.exit(1)

    file_path = sys.argv[1]

    if not Path(file_path).is_file():
        print('Invalid file path')
        sys.exit(1)

    env_vars = extract_environ(file_path)
    write_to_env(env_vars)
    print('.env file created successfully')
