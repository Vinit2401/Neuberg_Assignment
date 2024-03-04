# Mutate Multi-FASTA

## Introduction

This program is designed to mutate a multi-FASTA file. It takes as input an FASTA (gzip) file and a BED file specifying the regions to be mutated.

## Input Files

1. **influenza.fna.gz**: This file contains the original multi-FASTA sequence of the influenza virus. To download this file, please visit the [NCBI link](https://ftp.ncbi.nlm.nih.gov/genomes/INFLUENZA/).

2. **bed_file.bed**: This BED file contains the regions to be mutated in the FASTA file. It should be available in the current working directory.

   Note: The input FASTA file is provided in gzip format for convenience. The original FASTA file is approximately ~1.3 GB in size, which may be cumbersome to download and upload. Therefore, a gzip file is used as input here.

Make sure these files are present in your current working directory before running the program.

## How to Use

1. **Download Input Files**:
   - Download the `influenza.fna.gz` file from the provided NCBI link.
   - Ensure the `bed_file.bed` is available in your current working directory.

2. **Run the main.py script**:
   - Execute the main.py script.

3. **View Output**:
   - Once the program has completed execution, the mutated multi-FASTA file will be generated.
   - Output file name : mutated.fasta

## Notes

- The program utilizes the BED file format to specify the regions for mutation.
- Mutation operations : Replacing the first occurrence of adenine (A) with cytosine (C) in the subsequence

## Dependencies

- Python 3.x

#### Date of creation : 17 Feb 2024 | Developer : Vinit Gupta
