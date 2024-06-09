#I want to make a script that downloads sequences from NCBI based on taxonomic ID number
from Bio import Entrez
from Bio import SeqIO


# Set up the Entrez email
Entrez.email = "harleymount@hotmail.com"

# Search for the sequences
handle = Entrez.esearch(db="nucleotide", term="Ursus americanus")

# Fetch the records
record = Entrez.efetch(db="nucleotide", id=handle.read(), rettype="fasta")

file=open("sequences.fasta","w")


for seq_record in SeqIO.parse(record, "fasta"):
    file.write(seq_record.format("fasta"))
    
    
