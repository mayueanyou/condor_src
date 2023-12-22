# condor_src

DO NOT INSTALL ANYTHING WITH   `conda install`

USE `pip install` instead

## install miniconda

`wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh`

`bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3`

`eval "$(${HOME}/miniconda3/bin/conda shell.bash hook)"`

`conda init`

## if missing libGL.so.1

https://github.com/mayueanyou/libGL.so.1 

## condor functions

### check status

`condor_q`

### submit job

`condor_submit`

### remove job

`condor_rm`

### check priority 

`condor_userprio`
