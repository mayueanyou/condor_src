# condor_src

This repository contains tools/code for performing batch uploads for [HTCondor](https://htcondor.org/).

# Notice

To ignore issues.

DO NOT INSTALL ANYTHING WITH   `conda install`

USE `pip install` instead

## install miniconda

`wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh`

`bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3`

`eval "$(${HOME}/miniconda3/bin/conda shell.bash hook)"`

`conda init`

## quick start

`python3 submit.py`

## condor sumbit

### avoid a machine

`(Machine != "SURGE-OG-10-5-136-236")`

### avoid a GPU

`CUDADeviceName != "Quadro RTX 6000"`

## condor functions

### check gpus

`condor_status -compact -constraint 'TotalGPUs>0' -af:h machine TotalGPUs CUDADeviceName CUDACapability CUDADriverVersion CUDAGlobalMemoryMb CUDAComputeUnits CUDACoresPerCU HasNvidiaDriver`

### check status

`condor_q`

### submit job

`condor_submit`

### remove job

`condor_rm`

### check priority

`condor_userprio`
