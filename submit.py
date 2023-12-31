import os,sys,subprocess

def create_folder(path):
    if not os.path.exists(path):os.makedirs(path)

def get_sub_str(arguments):
    file_path=os.path.abspath(__file__)
    current_path =  os.path.abspath(os.path.dirname(file_path) + os.path.sep + ".")
    lines = [f'executable = {current_path}/conda_wrapper\n']
    lines.append('arguments = %s\n'%arguments)
    lines.append('error= ./err\noutput= ./out\nlog= ./log\n')
    lines.append('Requirements = (TotalGPUs > 0)\n+request_gpus = 1\nqueue')
    return lines

def condor_submit(path, py_file, py_arguments):
    create_folder(path)
    arguments = py_file + ' ' + py_arguments
    with open(path+"/sub", "w") as file:
        file.writelines(get_sub_str(arguments))
    subprocess.run(["rm log & condor_submit sub"], cwd=path, shell=True)

def quick_start():
    file_path=os.path.abspath(__file__)
    current_path =  os.path.abspath(os.path.dirname(file_path) + os.path.sep + ".")
    py_file = current_path + '/test.py'
    condor_submit(current_path + '/condor/test_1', py_file, '-str world_1')
    condor_submit(current_path + '/condor/test_2', py_file, '-str world_2')

if __name__ == '__main__':
    quick_start()
