import pandas as pd
df = pd.read_csv('database_accession_3star.tsv', sep='\t')
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
                           "DrugBank accession":"drugbank",
                           "MolBase accession":"molbase",
                           "COMe accession":None,
                           "RESID accession":"resid",
                           "LIPID MAPS class accession":None,
                           "Reaxys Registry Number":None,
                           "PDB accession":"pdb",
                           "Patent accession":None,
                           "WebElements accession":None,
                           "KNApSAcK accession":"knapsack",
                           "PubMed accession":"pubmed",
                           "Agricola citation":None,
                           "Chinese Abstracts citation":None,
                           "PubMed Central citation":None,
                           "CiteXplore citation":None,
                           "YMDB accession":None,
                           "ECMDB accession":None,
                           "Pesticides accession":None,
                           "SMID accession":None,
                           "Pubchem accession":"pubchem.compound",
                           "ChemIDplus accession":None,
                           "Drug Central accession":None,
                           "FAO/WHO standards accession":None,
                           "PPDB accession":None,
                           "VSDB accession":None,
                           "BPDB accession":None,
                           "PPR":None,
                           "GlyGen accession":None}

df.replace({"TYPE": thisdata2identifiersorg}, inplace=True)
df['identifiersorgprefix1'] = 'CHEBI'
df.rename(columns={'COMPOUND_ID': 'id1', 'TYPE': 'identifiersorgprefix2', 'ACCESSION_NUMBER': 'id2'}, inplace=True)
df = df[['identifiersorgprefix1', 'id1', 'identifiersorgprefix2', 'id2']]
