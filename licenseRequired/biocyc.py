import pybiopax
model = pybiopax.model_from_owl_file('biopax-level3.owl')
objs = model.objects

f = open('biocyc.tsv', 'w')
thisdb2other = {'Kegg Ligand':'kegg.compound', 'PubChem (CID)':'pubchem.compound', 'ChEBI': 'CHEBI', 'BIGG':'bigg.metabolite',
    'MetaNetX':'metanetx.chemical', 'Seed':'seed.compound', 'ZINC':'zinc', 'EchoBASE':'echobase', 'ASAP':'asap', 'UniProt':'uniprot',
    'NCBI Reference Sequences Database':'refseq', 'EcoliWiki':'ecoliwiki', 'Smart':'smart', 'InterPro':'interpro', 'Pfam':'pfam',
    'PubMed':'pubmed', 'ChemSpider':'chemspider', 'HMDB':'hmdb', 'DrugBank':'drugbank', 'CAS':'cas', 'MetaboLights':'metabolights',
    'Reactome':'reactome', 'Wikipedia':'wikipedia.en', 'Protein Data Bank':'pdb', 'SWISS-MODEL':'swiss-model', 'KEGG':'kegg.pathway',
    'Panther':'panther.family', 'KNApSAcK':'knapsack', 'UMBBD Compound':'umbbd.compound', 'Prosite':'prosite',
    'Database of Interacting Proteins':'dip', 'Swiss-Model':'swiss-model', 'CAZy':'cazy', 'Prints':'prints', 'NCBI Gene':'ncbigene',
    'PubChem SID':'pubchem.substance', 'Kegg Glycan':'kegg.glycan', 'LIPID MAPS':'lipidmaps'}
lines = []
for key in objs:
    if hasattr(objs[key], 'xref'):
        if len(objs[key].xref) > 0:
            if type(objs[key].xref[0]) != str:
                #print(objs[key].xref[0])
                theid = objs[key].xref[0].id
                if hasattr(objs[key], 'entity_reference'):
                    eref = objs[key].entity_reference
                    if hasattr(eref, 'xref'):
                        xrefs = eref.xref
                        for xref in xrefs:
                            tmp = []
                            # tmp.append(theid)
                            # print("ECOCYC ID: " + theid)
                            if hasattr(xref, 'db'):
                                if xref.db in thisdb2other:
                                    tmp.append(thisdb2other[xref.db])
                                    if xref.db == 'Reactome':
                                        tmp.append("R-ALL-" + xref.id)
                                    else:
                                        tmp.append(xref.id)
                                    if len(tmp) == 2:
                                        tmp.insert(0, "biocyc\tECOLI:" + theid)
                            if len(tmp) == 3:
                                lines.append('\t'.join(tmp) + '\n')
f.writelines(pd.unique(lines))
f.close()
