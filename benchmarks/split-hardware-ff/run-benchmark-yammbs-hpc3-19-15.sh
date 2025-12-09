#!/usr/bin/env bash
#SBATCH -J yammbs
#SBATCH --array=1-3
#SBATCH -p standard
#SBATCH -t 1-00:00:00
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=16gb
#SBATCH --account dmobley_lab
#SBATCH --nodelist=hpc3-19-15
#SBATCH --output slurm-%x.%A-%a.out

# ===================== conda environment =====================
. ~/.bashrc
conda activate yammbs-dataset-submission

export OE_LICENSE="/data/homezvol3/lilyw7/oe_license.txt"

REP=${SLURM_ARRAY_TASK_ID}

FF="protein"
FF="sage21"
FF="sage23"

echo "Running yammbs for $FF, for replicate $REP"

python benchmark-yammbs.py "hpc3-19-15/${FF}/rep-${REP}/input.yaml" 16

echo "done"
