import os,sys,subprocess

class CondorController:
    def __init__(self,base_path:str,py_file:str,condor_version:str='base',ignore_machine:list =[],extra_requirements:str='',gpu=True) -> None:
        self.base_path = base_path
        self.py_file = py_file
        self.condor_version = condor_version
        
        self.extra_requirements = extra_requirements
        self.condor_script_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".") + '/conda_wrapper'
        self.gpu = gpu
        
        self.default_ignore_machine = ['CRUSH-NODE-10-5-87-4','SURGE-OG-10-5-204-23','SURGE-OG-10-5-137-119',
                                        'SURGE-OG-10-5-141-225','SURGE-OG-10-5-141-211','CRUSH-NODE-10-5-33-10',
                                        'CRUSH-NODE-10-5-7-3']
        if len(ignore_machine)!=0: self.default_ignore_machine += ignore_machine
        self.ignore_machine = ''.join([f'&&(Machine != "{machine}")' for machine in self.default_ignore_machine])

    def generate_sub_str(self,arguments,path):
        lines = [f'executable = {self.condor_script_path}\n',
                    f'arguments = {self.condor_version} {arguments}\n',
                    f'error= {path}/err\n',
                    f'output= {path}/out\n',
                    f'log= {path}/log\n']
        if self.gpu:
            lines.append(f'Requirements = (TotalGPUs > 0){self.ignore_machine}{self.extra_requirements}\n')
            lines.append(f'+request_gpus = 1\n')
        else:
            lines.append(f'Requirements = (Machine != "Empty"){self.ignore_machine}{self.extra_requirements}\n')
        lines.append('queue')
        return lines
    
    def submit(self,sub_path, py_arguments='',sub=True):
        path = self.base_path + sub_path
        if not os.path.exists(path):os.makedirs(path)
        arguments = self.py_file + ' ' + py_arguments
        with open(path+"/sub", "w") as file:
            file.writelines(self.generate_sub_str(arguments,path))
        
        print(f"Generate Submission string: {arguments}")
        print(f"Generate Submission path: {path}")
        if sub: subprocess.run(["rm log & condor_submit sub"], cwd=path, shell=True)