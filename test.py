import os,sys,argparse

def main(args):
    print(f"hello {args.str}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-str', type=str)
    args = parser.parse_args()
    main(args)