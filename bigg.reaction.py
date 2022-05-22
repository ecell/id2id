import pandas as pd
df = pd.read_table("http://bigg.ucsd.edu/static/namespace/bigg_models_reactions.txt")
df['database_links'] = df['database_links'].str.split('; ')
df = df.explode('database_links')

df2 = df.drop(columns=['name', 'reaction_string', 'model_list', 'old_bigg_ids'])
df3 = df2['database_links'].str.split('/', expand=True)

result = pd.DataFrame({'id1': df2['bigg_id'], 'identifiersorg2': df3[3], 'id2': df3[4]})
result['idenfiersorg1'] = 'bigg.reaction'
result[['idenfiersorg1', 'id1', 'identifiersorg2', 'id2']].to_csv('bigg.reaction.csv', index=False)
