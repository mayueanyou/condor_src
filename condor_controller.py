import os,sys,subprocess

class CondorController:
    def __init__(self,base_path:str,py_file:str,condor_version:str='base',extra_requirements:str='') -> None:
        self.base_path = base_path
        self.py_file = py_file
        self.condor_version = condor_version
        self.extra_requirements = extra_requirements
        self.condor_script_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".") + '/conda_wrapper'
    
    def generate_sub_str(self,arguments,path):
        lines = [f'executable = {self.condor_script_path}\n',
                f'arguments = {self.condor_version} {arguments}\n',
                f'error= {path}/err\noutput= {path}/out\nlog= {path}/log\n',
                f'Requirements = (TotalGPUs > 0){self.extra_requirements}\n+request_gpus = 1\nqueue']
        return lines
    
    def submit(self,sub_path, py_arguments):
        path = self.base_path + sub_path
        if not os.path.exists(path):os.makedirs(path)
        arguments = self.py_file + ' ' + py_arguments
        with open(path+"/sub", "w") as file:
            file.writelines(self.generate_sub_str(arguments,path))
        subprocess.run(["rm log & condor_submit sub"], cwd=path, shell=True)


def quick_start():
    file_path = os.path.abspath(__file__)
    current_path =  os.path.abspath(os.path.dirname(file_path) + os.path.sep + ".")
    condor_controller = CondorController(base_path = current_path + '/condor/', py_file = current_path + '/test.py',condor_version='py3.10')
    condor_controller.submit(sub_path = 'test_1', py_arguments = '-str world_1')
    condor_controller.submit(sub_path = 'test_2', py_arguments = '-str world_2')

if __name__ == "__main__":
    quick_start()