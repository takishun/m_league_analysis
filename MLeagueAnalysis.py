#!/usr/bin/env python
# coding: utf-8

# In[11]:


#1 import library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import cluster, preprocessing, mixture
from sklearn.cluster import KMeans
import category_encoders as ce
import seaborn as sns
import random
get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


data = pd.read_csv('MLeague_players.csv')


# In[13]:


data['総局数/試合数'] = data['総局数'] / data['試合数']


# In[14]:


data['総局数/試合数'].hist()


# In[15]:


data = data.sort_values('総局数/試合数',ascending=False)


# In[16]:


data.columns


# In[17]:


data.head()


# In[18]:


data.index = data['選手名']
data[['選手名','試合数']].sort_values('試合数',ascending=True).plot(kind='barh',figsize=(10,5))


# In[19]:


data[['選手名','総局数']].sort_values('総局数',ascending=True).plot(kind='barh',figsize=(10,5))


# In[22]:


#グラフ用の色分けの設定
color_dict = dict({'u-next':'cyan',
                   'dribens':'lime',
                   'konami':'green',
                   'furinkazan':'red',
                   'sega_sammy':'blue',
                   'raiden':'orange',
                   'sakura':'pink',
                   'abemas':'olive'
                  })


# In[23]:


#チーム別で色分けしたプロット
# fig,ax = plt.subplots(figsize=(14,11))
plt.figure(figsize=(10,10))
sns.scatterplot(x='総局数',y='連対率',data=data,s=100,hue='チーム',alpha=0.7,palette=color_dict,sizes=(10,250))
for x, y, name in zip(data['総局数'], data['連対率'], data['選手名']):
    plt.text(x+random.randint(-10,10)*0.0005, y+random.randint(-10,10)*0.0003, name)
plt.grid()
plt.savefig('総局数_vs_連対率_散布図.png')


# In[24]:


#チーム別で色分けしたプロット
# fig,ax = plt.subplots(figsize=(14,11))
plt.figure(figsize=(10,10))
sns.scatterplot(x='総局数',y='試合数',data=data,s=100,hue='チーム',alpha=0.7,palette=color_dict,sizes=(10,250))
for x, y, name in zip(data['総局数'], data['試合数'], data['選手名']):
    plt.text(x+random.randint(-10,10)*0.0005, y+random.randint(-10,10)*0.0003, name)
plt.grid()


# In[52]:


fig,ax = plt.subplots(figsize=(14,11))
sns.heatmap(data[['連対率','1位','2位','3位','4位']].corr(),square=True,vmax=1,vmin=-1,center=0,robust=True,annot=True,cmap='coolwarm')
plt.savefig('連対率と順位の相関.png')


# In[26]:


data['アガリ率と放銃率の差']=data['アガリ率']-data['放銃率']


# In[27]:


data[['連対率','ポイント','平着']].sort_values('連対率',ascending=False)


# In[51]:


fig,ax = plt.subplots(figsize=(14,11))
sns.heatmap(data[['トップ率','リーチ率','放銃率','副露率','連対率']].corr(),square=True,vmax=1,vmin=-1,center=0,robust=True,annot=True,cmap='coolwarm')
plt.savefig('トップ率相関.png')


# In[29]:


data[['連対率']].sort_values('連対率',ascending=True).plot(kind='barh',figsize=(10,5))


# In[30]:


group = data.groupby('チーム').agg('mean')


# In[31]:


group


# In[32]:


group[['連対率']].plot(kind='bar',color='orange',figsize=(10,10))


# In[45]:


# Draw a scatter plot while assigning point colors and sizes to different
# variables in the dataset
f, ax = plt.subplots(figsize=(6.5, 6.5))

#グラフ用の色分けの設定
color_dict = dict({'u-next':'cyan',
                   'dribens':'lime',
                   'konami':'green',
                   'furinkazan':'red',
                   'sega_sammy':'blue',
                   'raiden':'orange',
                   'sakura':'pink',
                   'abemas':'olive'
                  })

sns.scatterplot(x="平均打点", y='放銃平均打点',data=group,s=100,hue='チーム',alpha=0.7,palette=color_dict)
for x, y, name in zip(group['平均打点'], group['放銃平均打点'], group.index):
    plt.text(x, y, name)
plt.grid()
plt.savefig('打点散布図.png')


# In[35]:


# Draw a scatter plot while assigning point colors and sizes to different
# variables in the dataset
f, ax = plt.subplots(figsize=(6.5, 6.5))

#グラフ用の色分けの設定
color_dict = dict({'u-next':'cyan',
                   'dribens':'lime',
                   'konami':'green',
                   'furinkazan':'red',
                   'sega_sammy':'blue',
                   'raiden':'orange',
                   'sakura':'pink',
                   'abemas':'olive'
                  })

sns.scatterplot(x="アガリ率", y='平均打点',data=group,s=100,hue='チーム',alpha=0.7,palette=color_dict)
for x, y, name in zip(group['アガリ率'], group['平均打点'], group.index):
    plt.text(x, y, name)
plt.grid()
plt.savefig('corr_agari_get.png')


# In[36]:


group = data.groupby('チーム').sum()


# In[37]:


group[['1位','2位','3位','4位']].plot(kind='bar',figsize=(10,10),subplots=True, layout=(2, 2))
plt.savefig('順位.png')


# In[38]:


group[['1位']].plot(kind='bar',figsize=(10,5))
plt.savefig('順位1.png')


# In[39]:


group[['2位']].plot(kind='bar',figsize=(10,5),color = 'orange')
plt.savefig('順位2.png')


# In[40]:


group[['3位']].plot(kind='bar',figsize=(10,5),color = 'green')
plt.savefig('順位3.png')


# In[41]:


group[['4位']].plot(kind='bar',figsize=(10,5),color = 'red')
plt.savefig('順位4.png')


# In[42]:


group_r=group[group.index=='abemas']
group_r[['1位','2位','3位','4位']].plot(kind='bar')
plt.grid()
plt.savefig('rank_abemas.png')


# In[43]:


fig,ax = plt.subplots(figsize=(14,11))
sns.heatmap(data[['連対率','1位','2位','3位','4位']].corr(),square=True,vmax=1,vmin=-1,center=0,robust=True,annot=True,cmap='coolwarm')
plt.savefig('連対率と順位の相関.png')


# In[49]:


for i in group.index:
    group_r=group[group.index==i]
    group_r[['1位','2位','3位','4位']].plot(kind='bar')
    plt.grid()
    plt.savefig(i+'.png')


# In[ ]:




