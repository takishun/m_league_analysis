#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import glob
import re

flist = glob.glob('data/*.csv')

df = pd.DataFrame()
for i in flist:
    data = pd.read_csv(i)
    data = data.T
    data.columns = data.iloc[0]
    data = data.iloc[1:]
    data.insert(0,'選手名',data.index)
    data.insert(0,'チーム',re.search('(?<=\/).*(?=\.)', i).group())
    data.reset_index(drop=True,inplace=True)
    df = pd.concat([df,data])

df.to_csv('MLeague_players.csv',index=False)


# In[2]:


df = pd.read_csv('MLeague_players.csv')


# In[3]:


df 


# In[4]:


flist = glob.glob('data/*.csv')


# In[5]:


flist


# In[108]:


df = pd.DataFrame()
for i in flist:
    data = pd.read_csv(i)
    data = data.T
    data.columns = data.iloc[0]
    data = data.iloc[1:]
    data['チーム'] = re.search('(?<=\/).*(?=\.)', i).group()
    df = pd.concat([df,data])

del df


# In[5]:


df = pd.read_csv(flist[0])


# In[110]:


df = df.T


# In[111]:


df.columns = df.loc['選手名']


# In[112]:


df.iloc[0]


# In[113]:


df.reset_index(inplace=True)


# In[6]:


df


# In[114]:


df


# In[132]:


del data,df


# In[ ]:




