#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import xfeat
from sklearn.manifold import TSNE
import math
get_ipython().run_line_magic('matplotlib', 'inline')

lists = pd.read_html('https://m-league.jp/stats')
img_dir = 'image'
df = pd.DataFrame()
teams = ['drivens','EX','sakura','konami','abemas','sega_summy','raiden','u-next']
j = 0
for i in lists:
    data = i
    data = data.T
    data.columns = data.iloc[0]
    data = data[1:]
    data['チーム'] = teams[j]
    j+=1
    df = pd.concat([df,data])
    
data = pd.DataFrame(df['総局数']/df['試合数'],columns = {'局数/試合数'})
X = df[['ポイント','総局数', '連対率', 'ベストスコア', '平均打点', '副露率', 'リーチ率', 'アガリ率', '放銃率', '放銃平均打点']]
X.reset_index(drop=True,inplace=True)
# X.drop('index',inplace=True,axis=1)
X.to_csv('corr_dat.csv',index=False)

a = pd.read_csv('corr_dat.csv')
fig,ax = plt.subplots(figsize=(20,8))
sns.heatmap(a.corr(),annot=True)
plt.savefig('corr.png')


# In[94]:


X.reset_index


# In[ ]:





# In[2]:


df['打点期待値'] = df['アガリ率']*df['平均打点']
print(df[['打点期待値']].sort_values('打点期待値',ascending=False))


# In[3]:


df[['打点期待値']].sort_values('打点期待値',ascending=True).plot(kind='barh',figsize=(10,5))
plt.savefig('打点期待値.png')


# In[4]:


df['放銃点期待値'] = df['放銃率']*df['放銃平均打点']
print(df[['放銃点期待値']].sort_values('放銃点期待値',ascending=False))


# In[5]:


df[['放銃点期待値']].sort_values('放銃点期待値',ascending=True).plot(kind='barh',figsize=(10,5),color='pink')
plt.savefig('放銃点期待値.png')


# In[6]:


fig,ax = plt.subplots(figsize=(8,8))
plt.scatter(df['放銃点期待値'],df['打点期待値'])
for x, y, name in zip(df['放銃点期待値'], df['打点期待値'], df.index):
    plt.text(x, y, name)
plt.grid()
plt.xlabel('放銃点期待値')
plt.ylabel('打点期待値')


# In[7]:


df[['総局数','チーム']].groupby('チーム').sum().plot(kind='barh',figsize=(8,5))


# In[8]:


sns.lmplot(x='放銃点期待値',y='打点期待値',data = df,fit_reg = False,hue='チーム')
for x, y, name in zip(df['放銃点期待値'], df['打点期待値'], df.index):
    plt.text(x, y, name)
plt.grid()
plt.savefig('期待値.png')


# In[9]:


df.columns


# In[15]:


import matplotlib.pyplot as plt
import pandas as pd
import pickle

#t-SNEで次元削減
from sklearn.manifold import TSNE

df.reset_index(inplace=True)
index_df = df[['index','チーム']]

df.drop('index',inplace=True,axis=1)
df.drop('チーム',inplace=True,axis=1)

X =df

X = df[['試合数', '総局数', 'ポイント', '平着', '1位', '2位', '3位', '4位', 'トップ率', '連対率',
       'ラス回避率', 'ベストスコア', '平均打点', '副露率', 'リーチ率', 'アガリ率', '放銃率', '放銃平均打点']]

tsne = TSNE(n_components=2, random_state = 0, perplexity = 30, n_iter = 1000)
X_embedded = tsne.fit_transform(X)

ddf = pd.concat([df, pd.DataFrame(X_embedded, columns = ['col1', 'col2'])], axis = 1)
ddf['チーム'] = index_df['チーム']
article_list = ddf['チーム'].unique()
ddf['選手名'] = index_df['index']

colors =  ["lightgreen", "red", "pink", "g", "orange", "cyan", "k", "b"]
plt.figure(figsize = (30, 30))
for i , v in enumerate(article_list):
    tmp_df = ddf[ddf['チーム'] == v]
    plt.scatter(tmp_df['col1'],  
                tmp_df['col2'],
                label = v,
                color = colors[i],
               s = 1500)

for x, y, name in zip(ddf['col1'], ddf['col2'],ddf['選手名']):
    plt.text(x+0.5, y, name,fontsize=18)

plt.legend(fontsize = 30)
plt.savefig('TSNE.png')


# In[109]:


ddf


# In[110]:


df


# In[ ]:




