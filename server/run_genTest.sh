#!/bin/bash
#SBATCH --job-name=gentest
#SBATCH --output=genTest.log
#SBATCH --ntasks=1
#SBATCH --mem=32gb
#SBATCH --cpus-per-task=16
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1


srun python gen_test.py
