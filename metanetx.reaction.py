import pandas as pd
df = pd.read_table("./reac_xref.tsv", skiprows=351)
df2 = df.drop(columns=['description'])
df3 = df2['#source'].str.split(':', expand=True)

idorgpref = []
for i in requests.get("https://registry.api.identifiers.org/restApi/namespaces?size=9999").json()['_embedded']['namespaces']:
    idorgpref.append(i['prefix'])
    
df4=df3[df3[0].isin(idorgpref)]
df5=df2[df3[0].isin(idorgpref)]

result = pd.DataFrame({'idenfiersorg2': df4[0], 'id2': df4[1], 'id1': df5['ID']})
result['idenfiersorg1'] = 'metanetx.reaction'
result = result[['idenfiersorg1', 'id1', 'idenfiersorg2', 'id2']]
result.to_csv('metanetx.reaction.csv', index=False)
