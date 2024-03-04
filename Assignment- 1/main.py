import gzip
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# Step 1: Unzipping the input file
input_file = "influenza.fna.gz"
output_file = "influenza.fasta"

with gzip.open(input_file, 'rt') as f_in:
    with open(output_file, 'w') as f_out:
        for line in f_in:
            f_out.write(line)

# Step 2: Extract and mutate subsequences from input fasta using custom bed file
bed_file = "bed_file.bed"

subsequences = []
with open(bed_file) as bed_handle:
    for line in bed_handle:
        parts = line.strip().split("\t")
        if len(parts) >= 3:  # Ensure at least 3 elements in the line
            gene_name = parts[0]
            start = int(parts[1])
            end = int(parts[2])
            subsequence = None
            with open(output_file, "r") as fasta_handle:
                for record in SeqIO.parse(fasta_handle, "fasta"):
                    subsequence = record.seq[start-1:end]  # Adjusting 0-based indexing
                    subsequence = subsequence.reverse_complement()  # Reverse complement the subsequence
                    mutated_seq = Seq(str(subsequence).replace("A", "C", 1))  # Replacing the first occurrence of adenine (A) with cytosine (C) in the subsequence
                    record.seq = record.seq[:start-1] + Seq(mutated_seq) + record.seq[end:]  # Replace old subsequence with mutated one
                    subsequences.append(record)

# Step 3: Write mutated sequences to new fasta file
mutated_fasta = "mutated.fasta"
with open(mutated_fasta, "w") as out_handle:
    SeqIO.write(subsequences, out_handle, "fasta")
