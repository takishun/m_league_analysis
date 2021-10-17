#!/usr/bin/env python
# coding: utf-8

# In[99]:


#1 import library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import cluster, preprocessing, mixture
from sklearn.cluster import KMeans
import category_encoders as ce
import seaborn as sns
import random


# In[27]:


get_ipython().system('conda install category_encoders -y')


# In[130]:


color_dict = dict({'u-next':'cyan',
                   'dribens':'lime',
                   'konami':'green',
                   'furinkazan':'red',
                   'sega_sammy':'blue',
                   'raiden':'orange',
                   'sakura':'pink',
                   'abemas':'olive'
                  })


# In[72]:


data = pd.read_csv('MLeague_players.csv')


# In[61]:


# Eoncodeしたい列をリストで指定。もちろん複数指定可能。
list_cols = ['チーム','選手名']

# 序数をカテゴリに付与して変換
ce_oe = ce.OrdinalEncoder(cols=list_cols,handle_unknown='impute')
df_session_ce_ordinal = ce_oe.fit_transform(data)

df_session_ce_ordinal.head()

data = data.join(df_session_ce_ordinal.add_suffix("_ordinal"))


# In[62]:


ce_oe.category_mapping


# In[63]:


test.head()


# In[59]:


test.columns


# In[139]:


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


# In[180]:


X = data[['試合数', '総局数', 'ポイント', '平着', '1位', '2位', '3位', '4位',
       'トップ率', '連対率', 'ラス回避率', 'ベストスコア', '平均打点', '副露率', 'リーチ率', 'アガリ率', '放銃率',
       '放銃平均打点']]
z = data['チーム']
sc=preprocessing.StandardScaler()
sc.fit(X)
X_norm=sc.transform(X)


# In[158]:


distortions = []
for i  in range(1,14):                # 1~10クラスタまで一気に計算 
    km = KMeans(n_clusters=i,
                init='k-means++',     # k-means++法によりクラスタ中心を選択
                n_init=10,
                max_iter=300,
                random_state=0)
    km.fit(X)                         # クラスタリングの計算を実行
    distortions.append(km.inertia_)   # km.fitするとkm.inertia_が得られる

plt.plot(range(1,14),distortions,marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.show()


# In[30]:


km = KMeans(n_clusters=6,init='k-means++',     # k-means++法によりクラスタ中心を選択
                n_init=10,
                max_iter=300,
                random_state=0)
km.fit(X_norm)
labels=km.predict(X_norm)


# In[181]:


#7 VBGMM
vbgm=mixture.BayesianGaussianMixture(n_components=10,random_state=6)
vbgm=vbgm.fit(X_norm)
labels=vbgm.predict(X_norm)

#9 the number of class is plotted with probability
plt.figure(figsize=(10,15))
plt.subplot(4,1,4)
x_tick=np.array([1,2,3,4,5,6,7,8,9,10])
plt.bar(x_tick,vbgm.weights_,width=0.7,tick_label=x_tick,color='orange')
plt.show()


# In[16]:


data['クラスタ'] = labels


# In[ ]:




