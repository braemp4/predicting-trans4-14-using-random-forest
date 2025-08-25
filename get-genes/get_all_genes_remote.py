import gene_mapper
import pandas as pd

rna_seq_df = pd.read_csv("data/raw_rnaseq.csv")
ids = rna_seq_df["Unnamed: 0"] 
rna_seq_df = rna_seq_df.rename(index = ids) #type: ignore
rna_seq_df = rna_seq_df.drop(rna_seq_df.columns[0], axis=1)

rna_seq_df = rna_seq_df[rna_seq_df.sum(axis = 1) > 0]

rna_seq_df = rna_seq_df.transpose()

gene_ids = rna_seq_df.columns

print(gene_ids)

gene_mapper = gene_mapper.GeneScraper(gene_ids)

gene_names = gene_mapper.get_gene_names()

rna_seq_df["gene_names"] = gene_names

rna_seq_df.to_csv("rna_seq_df_w_gene_ids.csv")



