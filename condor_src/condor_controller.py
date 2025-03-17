import os,sys,subprocess

class CondorController:
    def __init__(self,base_path:str,py_file:str,condor_version:str='base',ignore_machine:list =[],extra_requirements:str='') -> None:
        self.base_path = base_path
        self.py_file = py_file
        self.condor_version = condor_version
        self.ignore_machine = ''.join([f'&&(Machine != "{machine}")' for machine in ignore_machine])
        self.extra_requirements = extra_requirements
        self.condor_script_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".") + '/conda_wrapper'
    
    def generate_sub_str(self,arguments,path):
        lines = [f'executable = {self.condor_script_path}\n',
                f'arguments = {self.condor_version} {arguments}\n',
                f'error= {path}/err\n',
                f'output= {path}/out\n',
                f'log= {path}/log\n',
                f'Requirements = (TotalGPUs > 0){self.ignore_machine}{self.extra_requirements}\n',
                f'+request_gpus = 1\n',
                f'queue']
        return lines
    
    def submit(self,sub_path, py_arguments,sub=True):
        path = self.base_path + sub_path
        if not os.path.exists(path):os.makedirs(path)
        arguments = self.py_file + ' ' + py_arguments
        with open(path+"/sub", "w") as file:
            file.writelines(self.generate_sub_str(arguments,path))
        if sub: subprocess.run(["rm log & condor_submit sub"], cwd=path, shell=True)