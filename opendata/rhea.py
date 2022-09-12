import pandas as pd
df = pd.read_csv('rhea2xrefs.tsv', sep='\t')
df.drop(['DIRECTION', 'MASTER_ID'], axis=1, inplace=True)
tmp = df['DB'].map({'EC': 'ec-code', 'GO': 'GO', 'METACYC': 'metacyc.reaction', 'KEGG_REACTION': 'kegg.reaction', 'ECOCYC': 'biocyc', 'REACTOME': 'reactome', 'MACIE': 'macie'})
df['DB'] = tmp
tmp = df['ID'].str.replace('^GO:', '', regex=True)
df['ID'] = tmp
df['identifiersorgprefix1'] = "rhea"
df.rename(columns = {'RHEA_ID':'id1', 'ID':'id2', 'DB':'identifiersorgprefix2'}, inplace = True)
df = df[['identifiersorgprefix1', 'id1', 'identifiersorgprefix2', 'id2']]
tmp = 'ECOCYC:' + df[df['identifiersorgprefix2']=='biocyc']['id2']
df['id2'].loc[tmp.index] = tmp
