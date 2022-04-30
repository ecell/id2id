# !wget http://bigg.ucsd.edu/static/namespace/bigg_models_reactions.txt

import pandas as pd
a = pd.read_table("http://bigg.ucsd.edu/static/namespace/bigg_models_reactions.txt")
a[a['database_links'].str.contains("http://identifiers.org/kegg.reaction", na=False)].to_csv("bigg2kegg.csv")
