#!/usr/bin/env python3


#### Gathers and renames gff files from prokka output to prepare as roary input
####
#### Usage:
#### gather_gff_from_prokka.py -i [prokka_out] -o [roary_in]
####
#### Example:

import sys
import os
import shutil

import argparse

parser = argparse.ArgumentParser(description='Gather and rename gff files from prokka output so they can be queued with Roary')
parser.add_argument('-i', dest="input", metavar='Input folder', type=str,
                    help='Folder containing prokka outputs from all isolates')
parser.add_argument('-o', dest="output", metavar='Output folder', type=str,
                    help='Folder with renamed gff files that can be used as input for Roary')
args = parser.parse_args()
 


folder = args.input
out_folder = args.output

if not os.path.exists(out_folder):
	os.makedirs(out_folder)

files = os.listdir(folder)

for f in files:
	path = os.path.join(folder,f)
	files2 = os.listdir(path)
	for f2 in files2:
		if f2[-4:] == '.gff':
			src = os.path.join(path,f2)
			dst = os.path.join(out_folder,f)
			dst = dst+'.gff'
			print('copying '+src+' to '+dst)
			shutil.copy2(src,dst)
print("\nIf you want to run roary use\n")
print("sbatch -D . -c 8 --mem=24G --time=48:00:00 -J \"Roary\" -p daytime --wrap=\"roary -e --mafft -p 8 -f roary_out "+out_folder+"/*.gff\"")