import os,sys
from condor_src import CondorController

def submit_wrap(sub_path,py_arguments):
    file_path=os.path.abspath(__file__)
    current_path =  os.path.abspath(os.path.dirname(file_path) + os.path.sep + ".")
    cc = CondorController(base_path = current_path + '/condor/', 
                        py_file = current_path + '/test.py',
                        condor_version='py3.10',
                        ignore_machine=['CRUSH-NODE-10-5-87-4','SURGE-OG-10-5-204-23','SURGE-OG-10-5-137-119','SURGE-OG-10-5-141-225'])
    cc.submit(sub_path = sub_path, py_arguments = py_arguments,sub=True)


if __name__ == '__main__':
    submit_wrap('test_1','-str 1')
    submit_wrap('test_2','-str 2')