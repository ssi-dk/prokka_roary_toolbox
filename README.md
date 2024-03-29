# Prokka/Roary toolbox
Scripts for easily running prokka and roary on calc.
<br>



## Run Prokka

### Input
A directory containing genomic assemblies (.fa, .fna, .fasta)
<br>

### Output
A directory for each input-fasta file containing annotated output in a range of different formats (gbk, gff, faa, fna)
<br>
### Usage

*source activate env_prokka*<br>
*run_prokka_on_folder.py assemblies_directory prokka_out project*

<br><br>

## Run Roary

### Input
The output directory from prokka. Roary uses the input files from these which are first gathered and renamed for easier handling
<br>
### Usage

*gather_gff_from_prokka.py prokka_out roary_in*<br>
*source activate env_prokka*<br>
*sbatch -D . -c 8 --mem=24G --time=48:00:00 -J "Roary" -p daytime --wrap="roary -e --mafft -p 8 –f roary_out roary_in/\*.gff"*

<br><br>


## What does it do?

Prokka does genome annotation on individual fasta files, roary compares gene content between isolates and outputs a range of different plots and tables to be analyzed.
<br>



## Links

### Prokka
https://github.com/tseemann/prokka<br>
<br>
### Roary
https://sanger-pathogens.github.io/Roary/<br>
<br>
### Blast suite
https://www.ncbi.nlm.nih.gov/books/NBK279690/<br>
<br>
