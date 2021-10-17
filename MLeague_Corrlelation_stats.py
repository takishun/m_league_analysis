#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[11]:


data = pd.read_csv('MLeague_players.csv')


# In[18]:


data


# In[20]:


corr_columns = data[['ポイント','ラス回避率','リーチ率','トップ率','副露率','放銃率','アガリ率','放銃平均打点','平均打点','ベストスコア']]


# In[25]:


fig,ax = plt.subplots(figsize=(14,11))
sns.heatmap(corr_columns.corr(),square=True,vmax=1,vmin=-1,center=0,robust=True,annot=True,cmap='coolwarm')
plt.savefig('correlation.png')


# In[24]:





# In[ ]:




