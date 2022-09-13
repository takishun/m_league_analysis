#!/usr/bin/env python
# coding: utf-8

# In[71]:


import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import streamlit as st
# %matplotlib inline

fname = 'data/MLeague_stats2022-03-30.csv'

if __name__ == "__main__":
    df = pd.read_csv(fname)
    df.rename(columns={'Unnamed: 0': '選手名'},inplace=True)
    df.index = df['選手名']
    df.drop('選手名',axis = 1,inplace=True)
    
    st.title('Mリーグスタッツ')
    st.write(('データ取得日：'+ datetime.date.today().strftime('%Y/%m/%d')))
    
    st.header('個人成績テーブル')
    st.dataframe(df.sort_values('ポイント',ascending=False))
    
    st.header('個人ポイントランキング')
    arr = df[['ポイント']].sort_values('ポイント',ascending=False)
    fig,ax = plt.subplots(figsize=(8.0, 10.0))
    ax.barh(arr.index.to_list(),arr['ポイント'].to_list(),align = 'center',color='green')
    st.pyplot(fig)
    
    st.header('チームポイントランキング')
    mdf = df[['試合数','チーム', '総局数', 'ポイント', '1位', '2位', '3位', '4位']].groupby('チーム').sum()
    arr = mdf[['試合数', '総局数', 'ポイント', '1位', '2位', '3位', '4位']].sort_values('ポイント',ascending=False)
    fig,ax = plt.subplots(figsize=(8.0, 10.0))
    ax.barh(arr.index.to_list(),arr['ポイント'].to_list(),align = 'center',color='green')
    st.pyplot(fig)
    


# In[ ]:




