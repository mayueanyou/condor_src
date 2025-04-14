import os,sys,argparse
import torch
import pytorch_lib as ptl

def main(args):
    if torch.cuda.is_available():
        print(torch.cuda.get_device_name(0))
        print(torch.cuda.device_count())
    else:
        print('No GPU')
    print(f"hello {args.str}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-str', type=str)
    args = parser.parse_args()
    main(args)