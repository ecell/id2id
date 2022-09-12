import pandas as pd
df = pd.read_csv('compound_origins_3star.tsv', sep='\t')
df.drop(['ID', 'SOURCE'], axis=1, inplace=True)

thisdata2identifiersorg = {"KEGG COMPOUND accession":"kegg.compound",
                           "CAS Registry Number":"cas",
                           "GlyTouCan accession":"glytoucan",
                           "FooDB accession":"foodb.compound",
                           "MetaCyc accession":"metacyc.compound",
                           "Chemspider accession":"chemspider",
                           "HMDB accession":"hmdb",
                           "LINCS accession":"lincs.smallmolecule",
                           "UM-BBD compID":"umbbd.compound",
                           "Beilstein Registry Number":None,
                           "LIPID MAPS instance accession":"lipidmaps",
                           "KEGG DRUG accession":"kegg.drug",
                           "Gmelin Registry Number":None,
                           "PDBeChem accession":"pdb-ccd",
                           "KEGG GLYCAN accession":"kegg.glycan",
                           "Wikipeida accession":"wikipedia.en",
                           "DrugBank accession":"drugbank",}
