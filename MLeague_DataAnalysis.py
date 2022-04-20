#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 import library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import cluster, preprocessing, mixture
from sklearn.cluster import KMeans
import category_encoders as ce
import seaborn as sns
import random


# In[2]:


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


# In[3]:


data = pd.read_csv('MLeague_players.csv')


# In[4]:


data


# In[61]:


# Eoncodeしたい列をリストで指定。もちろん複数指定可能。
list_cols = ['チーム','選手名']

# 序数をカテゴリに付与して変換
ce_oe = ce.OrdinalEncoder(cols=list_cols,handle_unknown='impute')
df_session_ce_ordinal = ce_oe.fit_transform(data)

df_session_ce_ordinal.head()

data = data.join(df_session_ce_ordinal.add_suffix("_ordinal"))


# In[62]:


#エンコーディングのマッピング結果確認
ce_oe.category_mapping


# In[63]:


test.head()


# In[59]:


test.columns


# In[193]:


#チーム別で色分けしたプロット
plt.figure(figsize=(10,10))
sns.scatterplot(x='副露率',y='リーチ率',data=data,s=100,hue='チーム',alpha=0.7,palette=color_dict,size='平均打点',sizes=(10,250))
for x, y, name in zip(data['副露率'], data['リーチ率'], data['選手名']):
    plt.text(x+random.randint(-10,10)*0.0005, y+random.randint(-10,10)*0.0003, name)
plt.grid()


# In[185]:


X = data[[ '副露率', 'リーチ率']]
X.index = data['チーム']
z = data['チーム']
sc=preprocessing.StandardScaler()
sc.fit(X)
X_norm=sc.transform(X)


# In[189]:


km = KMeans(n_clusters=4,init='k-means++',     # k-means++法によりクラスタ中心を選択
                n_init=10,
                max_iter=300,
                random_state=0)
km.fit(X_norm)
labels=km.predict(X_norm)


# In[190]:


data['クラスタ'] = labels


# In[191]:


plt.figure(figsize=(10,10))
sns.scatterplot(x='副露率',y='リーチ率',data=data,s=100,hue='クラスタ',palette='bright',size='平均打点',sizes=(10,250))
# plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],s=250,marker='*',c='red')
for x, y, name in zip(data['副露率'], data['リーチ率'], data['選手名']):
    plt.text(x+random.randint(-10,10)*0.0005, y+random.randint(-10,10)*0.0003, name)
plt.grid()


# In[192]:


data.to_csv('result.csv',encoding='cp932')


# In[ ]:




