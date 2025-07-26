#!/bin/bash
#SBATCH --job-name=stab-ddg-run
#SBATCH --partition=debug
#SBATCH --nodes="1"
#SBATCH --ntasks-per-node="1"
#SBATCH --cpus-per-task=16
#SBATCH --gpus-per-task=1
#SBATCH --mem-per-cpu=2G
#SBATCH --time=02:00:00
#SBATCH --output=build1.stdout
#SBATCH --error=build1.stderr

# eventually load other modules
#module purge
#module load Package1 Package2 Package3

# go to the (current) working directory (optional, if this is the
# directory where you submitted the job)

echo Start Job
date

APPTAINER_CACHEDIR=/tmp/ \
APPTAINER_TMPDIR=/tmp/ \
apptainer exec $VSC_SCRATCH/stab-ddg-v1.sif python run_stabddg.py \
        --pdb_path examples/one_mutation/1AO7.pdb \
        --mutation EA63Q,QD30V,KA66A --chains ABC_DE

date
echo End Job
