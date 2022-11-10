#!/usr/bin/env python3


#### Runs prokka on a directory of fasta assemblies
####
#### Usage:
#### run_prokka_on_folder.py -i [assembly_dir] -o [prokka_out] -p [partition]
####
#### Example:
import os
import sys
import argparse

parser = argparse.ArgumentParser(description='Run Prokka on all fasta files in an input folder (.fa, .fna, .fasta)')
parser.add_argument('-i', dest="input", metavar='Input folder', type=str,
                    help='Input folder containing genomic assemblies')
parser.add_argument('-o', dest="output", metavar='Output folder', type=str,
                    help='Output folder. Output folder will contain a subfolder for each input-fasta file with annotated genome')
parser.add_argument('-q', dest="queue_system", metavar='queue_system',type=str, default = "slurm", help='Queue system to use. Default \"slurm\", alternative \'none\'')
parser.add_argument('-p', dest="partition", metavar='partition',type=str, default = "project", help='Partition to run jobs on. Default \"project\"')
args = parser.parse_args()
 



in_dir = args.input
out_dir = args.output
partition = args.partition

files = os.listdir(in_dir)

if not os.path.exists(out_dir):
	os.makedirs(out_dir)

for file in files:
	split = file.split(".")
	if split[-1] == "fa" or split[-1] == "fna" or split[-1] == "fasta":
		ID = ".".join(split[:-1])
		path = os.path.join(in_dir,file)
		out_path = os.path.join(out_dir,ID)
		if args.queue_system == "slurm":
			cmd = "sbatch -D . -c 2 --mem=4G --time=4:00:00 -J \"Prokka\" -p "+partition+" --wrap=\"prokka "+path+" --outdir "+out_path+" --compliant --force\""
		else:
			cmd = "prokka "+path+" --outdir "+out_path+" --compliant --force"
		os.system(cmd)
		print(cmd)

