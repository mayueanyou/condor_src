import os,argparse
from .condor_controller import CondorController

# cc = CondorController(base_path = current_path + '/condor/', 
#                         py_file = current_path + '/main.py',
#                         condor_version='py3.10',
#                         gpu = gpu)

if __name__ == "__main__":
    current_path = os.getcwd()
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--file_name', type=str,required=True, help='Name of the python file to run')
    parser.add_argument('-s','--sub_name', type=str)
    parser.add_argument('-g', '--gpu', action='store_true', default=False, help='Use GPU')
    parser.add_argument('-cv', '--conda_version', type=str, default='base', help='Conda environment version to use')
    args = parser.parse_args()
    cc = CondorController(base_path = current_path + '/condor/', 
                        py_file = current_path + f'/{args.file_name}',
                        condor_version=args.conda_version,
                        gpu = args.gpu)
    sub_path = args.file_name.split('.')[0]
    if args.sub_name is not None: sub_path += f'/{args.sub_name}'
    cc.submit(sub_path = sub_path, sub=True)