import os,sys,subprocess

def create_folder(path):
    if not os.path.exists(path):os.makedirs(path)

def get_sub_str(arguments,condor_version,path,extra_requirements=''):
    file_path=os.path.abspath(__file__)
    current_path =  os.path.abspath(os.path.dirname(file_path) + os.path.sep + ".")
    lines = [f'executable = {current_path}/conda_wrapper\n']
    lines.append(f'arguments = {condor_version} {arguments}\n')
    lines.append(f'error= {path}/err\noutput= {path}/out\nlog= {path}/log\n')
    lines.append(f'Requirements = (TotalGPUs > 0){extra_requirements}\n+request_gpus = 1\nqueue')
    return lines

def condor_submit(path, py_file, py_arguments, condor_version = 'base',extra_requirements=''):
    create_folder(path)
    arguments = py_file + ' ' + py_arguments
    with open(path+"/sub", "w") as file:
        file.writelines(get_sub_str(arguments,condor_version,path,extra_requirements))
    subprocess.run(["rm log & condor_submit sub"], cwd=path, shell=True)

def submit_wrap_demo(folder,argument):
    current_path =  os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".")
    path = current_path + '/condor/' + folder
    py_file = current_path + '/test.py'
    py_arguments = argument
    condor_version = 'base'
    extra_requirements = ''
    condor_submit(path = path, py_file = py_file, py_arguments=py_arguments, condor_version=condor_version,extra_requirements=extra_requirements)

def quick_start():
    file_path=os.path.abspath(__file__)
    current_path =  os.path.abspath(os.path.dirname(file_path) + os.path.sep + ".")
    py_file = current_path + '/test.py'
    condor_submit(current_path + '/condor/test_1', py_file, '-str world_1','py3.10')
    condor_submit(current_path + '/condor/test_2', py_file, '-str world_2','py3.10')

def quick_start_wrap():
    submit_wrap_demo('test_1','-str world_1')
    submit_wrap_demo('test_2','-str world_2')

if __name__ == '__main__':
    #quick_start()
    quick_start_wrap()