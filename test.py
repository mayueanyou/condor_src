import os,sys,argparse
import torch

def main(args):
    print(torch.cuda.get_device_name(0))  if torch.cuda.is_available() else print('No GPU')
    print(f"hello {args.str}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-str', type=str)
    args = parser.parse_args()
    main(args)