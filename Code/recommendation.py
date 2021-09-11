# import pandas library
# import seaborn library
# import matplotlib library
#%%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Get the data
column_names = ['user_id', 'item_id', 'rating', 'timestamp']

path = 'file.tsv'

df = pd.read_csv(path, sep='\t', names=column_names)

# Check the head of the data
df.head(10)
#%%
# Check out all the movies and their respective IDs
movie_titles = pd.read_csv('Movie_Id_Titles.csv')
movie_titles.head(10)
#
data = pd.merge(df, movie_titles, on='item_id')
data.head(10)
#
# Calculate mean rating of all movies
data.groupby('title')['rating'].mean().sort_values(ascending=False).head(10)
#
# Calculate count rating of all movies
data.groupby('title')['rating'].count().sort_values(ascending=False).head(10)
#
# creating dataframe with 'rating' count values
ratings = pd.DataFrame(data.groupby('title')['rating'].mean())

ratings['num of ratings'] = pd.DataFrame(
    data.groupby('title')['rating'].count())

ratings.head()
#
sns.set_style('white')
%matplotlib inline

# plot graph of 'num of ratings column'
plt.figure(figsize=(10, 4))
ratings['num of ratings'].hist(bins=70)

# plot graph of 'ratings' column
plt.figure(figsize=(10, 4))
ratings['rating'].hist(bins=70)

# Sorting values according to
# the 'num of rating column'
moviemat = data.pivot_table(index='user_id', columns='title', values='rating')
moviemat.head(10)
#
ratings.sort_values('num of ratings', ascending=False).head(10)
#
# analysing correlation with similar movies
starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']

starwars_user_ratings.head(10)
#
# analysing correlation with similar movies
similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)

corr_starwars = pd.DataFrame(similar_to_starwars, columns=['Correlation'])
corr_starwars.dropna(inplace=True)

corr_starwars.head(10)
#
# Similar movies like starwars
corr_starwars.sort_values('Correlation', ascending=False).head(10)
#
corr_starwars = corr_starwars.join(ratings['num of ratings'])

corr_starwars.head(10)
#
corr_starwars[corr_starwars['num of ratings'] > 100].sort_values('Correlation', ascending=False).head(10)
#
# Similar movies as of liarliar
corr_liarliar = pd.DataFrame(similar_to_liarliar, columns=['Correlation'])
corr_liarliar.dropna(inplace=True)

corr_liarliar = corr_liarliar.join(ratings['num of ratings'])
corr_liarliar[corr_liarliar['num of ratings'] > 100].sort_values('Correlation', ascending=False).head(10)
#


