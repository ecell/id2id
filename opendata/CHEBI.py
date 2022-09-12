import pandas as pd
df = pd.read_csv('compound_origins_3star.tsv', sep='\t')
df.drop(['ID', 'SOURCE'], axis=1, inplace=True)
thisdata2identifiersorg = {"KEGG COMPOUND accession":"kegg.compound",
                           "CAS Registry Number":"cas",
                           "GlyTouCan accession":"glytoucan",
                           "FooDB accession":"foodb.compound",
                           "MetaCyc accession":"metacyc.compound",
                           "Chemspider accession":"chemspider",
                           "HMDB accession":"hmdb",}
