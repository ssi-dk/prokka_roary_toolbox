#!/usr/bin/env python3

import os
import sys

def get_faa_filename(dir):
	for file in os.listdir(dir):
		if file.endswith(".faa"):
			return(file)


def get_ffn_filename(dir):
	for file in os.listdir(dir):
		if file.endswith(".ffn"):
			return(file)

def combine_faa_fasta(prokka_dir,faa_fasta):
	o = open(faa_fasta,'w')
	IDs = os.listdir(prokka_dir)
	print_line = ""
	for ID in IDs:
		isolate_dir = os.path.join(prokka_dir,ID)
		in_file = os.path.join(isolate_dir,get_faa_filename(isolate_dir))
		with open(in_file) as f:
			for line in f:
				if line.startswith('>'):
					line = line.replace(' ','_')
					line = ">"+ID+"__"+line[1:]
				print_line += line
	o.write(print_line)
	o.close()


def combine_ffn_fasta(prokka_dir,ffn_fasta):
	o = open(ffn_fasta,'w')
	IDs = os.listdir(prokka_dir)
	print_line = ""
	for ID in IDs:
		isolate_dir = os.path.join(prokka_dir,ID)
		in_file = os.path.join(isolate_dir,get_faa_filename(isolate_dir))
		with open(in_file) as f:
			for line in f:
				if line.startswith('>'):
					line = line.replace(' ','_')
					line = ">"+ID+"__"+line[1:]
				print_line += line
	o.write(print_line)
	o.close()

def setup_ffn_blast_db(ffn_fasta,blast_db_dir):
	cmd = "makeblastdb -in "+ffn_fasta+" -out "+blast_db_dir+" -dbtype nucl"
	print(cmd)
	os.system(cmd)

def setup_ffa_blast_db(ffa_fasta,blast_db_dir):
	cmd = "makeblastdb -in "+ffa_fasta+" -out "+blast_db_dir+" -dbtype prot"
	print(cmd)
	os.system(cmd)


prokka_dir = sys.argv[1]
blast_DB_dir = sys.argv[2]
if not os.path.exists(blast_DB_dir):
	os.makedirs(blast_DB_dir)

faa_fasta_path = os.path.join(blast_DB_dir,"prokka_combined.faa")
faa_blast_DB = os.path.join(blast_DB_dir,"prokka_faa")
ffn_fasta_path = os.path.join(blast_DB_dir,"prokka_combined.ffn")
ffn_blast_DB = os.path.join(blast_DB_dir,"prokka_ffn")

print("Combining prokka faa files to single fasta in "+faa_fasta_path)
combine_faa_fasta(prokka_dir,faa_fasta_path)

print("Setting up faa blast DB in "+ffn_blast_DB)
setup_ffa_blast_db(faa_fasta_path,faa_blast_DB)

print("Combining prokka ffn files to single fasta in "+ffn_fasta_path)
combine_ffn_fasta(prokka_dir,ffn_fasta_path)

print("Setting up faa blast DB in "+ffn_blast_DB)
setup_ffa_blast_db(faa_fasta_path,faa_blast_DB)

