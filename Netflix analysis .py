#!/usr/bin/env python
# coding: utf-8

# # Analysis of NETFLIX Streaming

# In[ ]:


import pandas as pd
df=pd.read_csv("netflix_titles.csv")
df


# In[ ]:


netflix=pd.read_csv("netflix_titles.csv")
netflix.isnull().sum()


# In[ ]:


netflix.nunique()


# In[ ]:


netflix.duplicated().sum()


# In[ ]:


import numpy as np
import plotly.express as px 
dff= pd.read_csv("netflix_titles.csv")
dff.shape


# In[ ]:


dff= pd.read_csv("netflix_titles.csv")
import plotly.express as px 
z = dff.groupby(['rating']).size().reset_index(name='counts')
pieChart = px.pie(z, values='counts', names='rating',
title='Distribution of Content Ratings on Netflix',
color_discrete_sequence=px.colors.qualitative.Set3)
pieChart.show()



# In[ ]:


dff['director']=dff['director'].fillna('No Director Specified')
filtered_directors=pd.DataFrame()
filtered_directors=dff['director'].str.split(',',expand=True).stack()
filtered_directors=filtered_directors.to_frame()
filtered_directors.columns=['Director']
directors=filtered_directors.groupby(['Director']).size().reset_index(name='Total Content')
directors=directors[directors.Director !='No Director Specified']
directors=directors.sort_values(by=['Total Content'],ascending=False)
directorsTop5=directors.head()
directorsTop5=directorsTop5.sort_values(by=['Total Content'])
fig1=px.bar(directorsTop5,x='Total Content',y='Director',title='Top 5 Directors on Netflix')
fig1.show()


# In[ ]:


dff['cast']=dff['cast'].fillna('No Cast Specified')
filtered_cast=pd.DataFrame()
filtered_cast=dff['cast'].str.split(',',expand=True).stack()
filtered_cast=filtered_cast.to_frame()
filtered_cast.columns=['Actor']
actors=filtered_cast.groupby(['Actor']).size().reset_index(name='Total Content')
actors=actors[actors.Actor !='No Cast Specified']
actors=actors.sort_values(by=['Total Content'],ascending=False)
actorsTop5=actors.head()
actorsTop5=actorsTop5.sort_values(by=['Total Content'])
fig2=px.bar(actorsTop5,x='Total Content',y='Actor', title='Top 5 Actors on Netflix')
fig2.show()


# In[ ]:


df1=dff[['type','release_year']]
df1=df1.rename(columns={"release_year": "Release Year"})
df2=df1.groupby(['Release Year','type']).size().reset_index(name='Total Content')
df2=df2[df2['Release Year']>=2010]
fig3 = px.line(df2, x="Release Year", y="Total Content", color='type',title='Trend of content produced over the years on Netflix')
fig3.show()


# In[ ]:


df=pd.read_csv("netflix_titles.csv")
df_netflix = pd.read_csv("netflix_titles.csv")
import matplotlib.pyplot as plt
import seaborn as sns
print (df_netflix.shape)
df_netflix.head()


# In[ ]:


import itertools 
list_country = [x.split(', ') for x in df_netflix.dropna(subset=['country'])['country'].tolist()]
list_country = list(itertools.chain(*list_country))

from collections import Counter
df_netflix_country_count = pd.DataFrame(Counter(list_country).most_common()[:10], columns=['Country', 'Count'])
plt.figure(figsize=(12,10))
sns.set(style="darkgrid")
ax = sns.barplot(y="Country", x='Count', data=df_netflix_country_count, palette="Set2", orient='h')

