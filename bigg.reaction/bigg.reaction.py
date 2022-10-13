import pandas as pd
df = pd.read_table("bigg_models_reactions.txt")
df2 = df.drop(columns=['name', 'reaction_string', 'model_list', 'old_bigg_ids'])
df2['database_links'] = df2['database_links'].str.split('; ')
df2 = df2.explode('database_links')
df3 = df2['database_links'].str.split('/', expand=True)
result = pd.DataFrame({'id1': df2['bigg_id'], 'identifiersorgprefix2': df3[3], 'id2': df3[4]})
result['identifiersorgprefix1'] = 'bigg.reaction'
result[['identifiersorgprefix1', 'id1', 'identifiersorgprefix2', 'id2']].to_csv('bigg.reaction.tsv', index=False, sep="\t")
