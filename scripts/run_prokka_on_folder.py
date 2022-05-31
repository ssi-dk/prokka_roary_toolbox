#!/usr/bin/env python3


#### Runs prokka on a directory of fasta assemblies
####
#### Usage:
#### run_prokka_on_folder.py [assembly_dir] [prokka_out] [partition]
####
#### Example:



import os
import sys

in_dir = sys.argv[1]
out_dir = sys.argv[2]
if len(sys.argv) > 3:
	partition = sys.argv[3]
else:
	partition = "project"

files = os.listdir(in_dir)

if not os.path.exists(out_dir):
	os.makedirs(out_dir)

for file in files:
	split = file.split(".")
	if split[-1] == "fa" or split[-1] == "fna" or split[-1] == "fasta":
		ID = ".".join(split[:-1])
		path = os.path.join(in_dir,file)
		out_path = os.path.join(out_dir,ID)
		cmd = "sbatch -D . -c 2 --mem=4G --time=4:00:00 -J \"Prokka\" -p "+partition+" --wrap=\"prokka "+path+" --outdir "+out_path+" --compliant --force\""
		os.system(cmd)
		print(cmd)

