import subprocess as subprocess_lib

def check_main_proc():
    print('main proc runing...')

def test_proc():
    print('test_proc runing...')

try:
    process_out = subprocess_lib.run([check_main_proc(),  ''], shell=True, check=True)
    process_out_test = subprocess_lib.run([test_proc(), ''], shell=True, check=True)
except subprocess_lib.CalledProcessError as erorr:
    print(f"Error in call: {erorr.cmd}!")
