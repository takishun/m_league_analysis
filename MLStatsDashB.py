#!/usr/bin/env python
# coding: utf-8

# In[71]:


import pandas as pd
import datetime
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import streamlit as st
# %matplotlib inline

fname = 'data/MLeague_stats2022-03-30.csv'

if __name__ == "__main__":
    df = pd.read_csv(fname)
    df.rename(columns={'Unnamed: 0': '選手名'},inplace=True)
    df.index = df['選手名']
    df.drop('選手名',axis = 1,inplace=True)
    
    st.title('Mリーグスタッツ')
    st.write(('データ取得日：2022/04/30'))
    st.write('Mリーグ選手成績データ可視化サイトです。')
    st.markdown('公式サイトはこちら:<a href = "https://m-league.jp/">Mリーグサイト</a>',unsafe_allow_html=True)
    
    st.header('個人ポイントランキング')
    st.dataframe(df.sort_values('ポイント',ascending=False))
    
    arr = df[['ポイント']].sort_values('ポイント',ascending=True)
    fig,ax = plt.subplots(figsize=(8.0, 8.0))
    ax.barh(arr.index.to_list(),arr['ポイント'].to_list(),align = 'center',color='green')
    ax.grid()
    st.pyplot(fig)
    
    st.header('チームポイントランキング')
    mdf = df[['試合数','チーム', '総局数', 'ポイント', '1位', '2位', '3位', '4位']].groupby('チーム').sum()
    mdf[['試合数', '総局数', 'ポイント', '1位', '2位', '3位', '4位']] = mdf[['試合数', '総局数', 'ポイント', '1位', '2位', '3位', '4位']].astype(int)
    st.dataframe(mdf[['試合数', '総局数', 'ポイント', '1位', '2位', '3位', '4位']].sort_values('ポイント',ascending=False))
    arr = mdf[['試合数', '総局数', 'ポイント', '1位', '2位', '3位', '4位']].sort_values('ポイント',ascending=True)
    fig,ax = plt.subplots(figsize=(8.0, 8.0))
    ax.barh(arr.index.to_list(),arr['ポイント'].to_list(),align = 'center',color='green')
    ax.grid()
    st.pyplot(fig)
    
    st.header('アガリ率と放銃率')
    fig,ax = plt.subplots(figsize=(8.0,8.0))
    plt.grid()
    mean_df = df[['チーム','ベストスコア','トップ率', '連対率','平均打点','放銃平均打点',
           'ラス回避率', '副露率', 'リーチ率', 'アガリ率', '放銃率']].groupby('チーム').mean()
    sns.scatterplot(data=mean_df,x = '放銃率',y='アガリ率',hue='チーム')
    for x, y, name in zip(mean_df['放銃率'], mean_df['アガリ率'], mean_df.index):
        plt.text(x, y, name)
    st.pyplot(fig)

    st.header('平均打点と放銃平均打点')
    fig,ax = plt.subplots(figsize=(8,8))
    plt.grid()
    sns.scatterplot(data=mean_df,x = '放銃平均打点',y='平均打点',hue='チーム')
    for x, y, name in zip(mean_df['放銃平均打点'], mean_df['平均打点'], mean_df.index):
        plt.text(x, y, name)
    st.pyplot(fig)
    

