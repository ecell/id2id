import pandas as pd
df = pd.read_table("bigg_models_metabolites.txt")
df2 = df.drop(columns=['bigg_id', 'name', 'model_list', 'old_bigg_ids'])
df2['database_links'] = df2['database_links'].str.split('; ')
df2 = df2.explode('database_links')
df3 = df2['database_links'].str.split('/', expand=True)
result = pd.DataFrame({'id1': df2['universal_bigg_id'], 'identifiersorgprefix2': df3[3], 'id2': df3[4]})
result['identifiersorgprefix1'] = 'bigg.metabolite'
result[['identifiersorgprefix1', 'id1', 'identifiersorgprefix2', 'id2']].to_csv('bigg.metabolite.tsv', header=False, index=False, sep="\t")
