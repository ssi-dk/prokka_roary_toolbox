# prokka_roary_toolbox
Scripts for running prokka and roary on calc.




## Usage

### Input
A directory containing genomic assemblies (.fa, .fna, .fasta)

### Run prokka

run_prokka_on_folder.py [assembly_dir] [prokka_out] [partition]

source activate env_prokka
run_prokka_on_folder.py assemblies prokka_out project


### Once finished, gather the gff files

gather_gff_from_prokka.py [prokka_out] [roary_in]

gather_gff_from_prokka.py prokka_out roary_in



### Then run roary
source activate env_prokka
sbatch -D . -c 8 --mem=24G --time=48:00:00 -J "Roary" -p daytime --wrap="roary -e --mafft -p 8 –f roary_out roary_in/*.gff"


## What does it do?

Prokka does genome annotation
