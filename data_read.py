import pandas as pd

name_basics = pd.read_csv("C:/Projects/data/name.basics.tsv", sep="\t", low_memory=False)
title_akas = pd.read_csv("C:/Projects/data/title.akas.tsv", sep="\t", low_memory=False)
title_basics = pd.read_csv("C:/Projects/data/title.basics.tsv", sep="\t", low_memory=False)
title_crew = pd.read_csv("C:/Projects/data/title.crew.tsv", sep="\t", low_memory=False)
title_episode = pd.read_csv("C:/Projects/data/title.episode.tsv", sep="\t", low_memory=False)
title_principals = pd.read_csv("C:/Projects/data/title.principals.tsv", sep="\t", low_memory=False)
title_ratings = pd.read_csv("C:/Projects/data/title.ratings.tsv", sep="\t", low_memory=False)

print(name_basics.head())
print(title_ratings.head())
