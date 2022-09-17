import pandas as pd
df = pd.read_csv('ECOLI_83333_idmapping.dat', sep='\t', header=None)

thisdata2identifiersorg = {
    'UniProtKB-ID':None, 'Gene_Name':None,'Gene_OrderedLocusName':None, 'GI':None, 'UniRef100':None,
    'UniRef90':None, 'UniRef50':None, 'UniParc':'uniparc', 'EMBL':None, 'EMBL-CDS':None,
    'NCBI_TaxID':'taxonomy', 'RefSeq':'refseq', 'RefSeq_NT':None, 'PDB':'pdb', 'BioGRID':'biogrid',
    'DIP':'dip', 'STRING':'string', 'ChEMBL':'chembl', 'DrugBank':'drugbank', 'EnsemblGenome':'ensembl',
    'EnsemblGenome_TRS':None, 'EnsemblGenome_PRO':None, 'GeneID':None, 'KEGG':None, 'PATRIC':None,
    'EchoBASE':'echobase', 'eggNOG':'eggnog', 'HOGENOM':'hogenom', 'OMA':'oma.protein', 'BioCyc':'biocyc',
    'CRC64':None, 'Gene_Synonym':None, 'UniPathway':None, 'Gene_ORFName':None, 'MEROPS':'merops', 'TCDB':'tcdb',
    'ComplexPortal':'complexportal', 'DNASU':None, 'MINT':None, 'ESTHER':None, 'PeroxiBase':'peroxibase', 'CollecTF':None,
    'PHI-base':None, 'Allergome':'allergome', 'DisProt':'disprot', 'REBASE':'rebase', 'SwissLipids':None, 'Reactome':'reactome'
}

df.replace({1: thisdata2identifiersorg}, inplace=True)
df.drop(df[df[1].isnull()].index, inplace=True)
df['identifiersorgprefix1'] = 'uniprot'
df.rename(columns={0:'id1', 1:'identifiersorgprefix2', 2:'id2'}, inplace=True)
df = df[['identifiersorgprefix1', 'id1', 'identifiersorgprefix2', 'id2']]
df.to_csv('uniprot.csv', index=False)
