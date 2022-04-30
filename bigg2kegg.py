import pandas as pd
df = pd.read_table("http://bigg.ucsd.edu/static/namespace/bigg_models_reactions.txt")
df['database_links'] = df['database_links'].str.split('; ')
df = df.explode('database_links')
df.head()
