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

fname = 'data/MLeague_stats.csv'

if __name__ == "__main__":
    df = pd.read_csv(fname)
    df.rename(columns={'Unnamed: 0': '選手名'},inplace=True)
    df.index = df['選手名']
    df.drop('選手名',axis = 1,inplace=True)
    
    st.title('Mリーグ2022-2023スタッツサイト')
#     st.write(('更新日：2022/10/15'))
    st.write('Mリーグ選手成績データ可視化サイトです。')
    st.write('現在は2022-2023レギュラーシーズン成績を可視化しています。')
    st.markdown('<a href = "https://m-league.jp/">公式サイトはこちら</a>',unsafe_allow_html=True)
    st.markdown('<a href="https://px.a8.net/svt/ejp?a8mat=3N26CN+5YCTU+4EKC+5YJRM" rel="nofollow">MリーグはABEMAで見れます！</a><img border="0" width="1" height="1" src="https://www18.a8.net/0.gif?a8mat=3N26CN+5YCTU+4EKC+5YJRM" alt="">',unsafe_allow_html=True)
    
    st.header('タイトル選手')
    col1, col2, col3 = st.columns(3)
    col1.metric('ベストスコア: '+df['ベストスコア'].sort_values(ascending=False).keys()[0], df['ベストスコア'].sort_values(ascending=False)[0].astype(int))
    col2.metric('ラス回避率: '+df['ラス回避率'].sort_values(ascending=False).keys()[0], df['ラス回避率'].sort_values(ascending=False)[0])
    col3.metric('ポイント: '+df['ポイント'].sort_values(ascending=False).keys()[0], df['ポイント'].sort_values(ascending=False)[0].astype(int))
    
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
    
    st.header('アガリ率vs放銃率')
    fig,ax = plt.subplots(figsize=(8.0,8.0))
    plt.grid()
    mean_df = df[['チーム','ベストスコア','トップ率', '連対率','平均打点','放銃平均打点',
           'ラス回避率', '副露率', 'リーチ率', 'アガリ率', '放銃率']].groupby('チーム').mean()
    sns.scatterplot(data=mean_df,x = '放銃率',y='アガリ率',hue='チーム')
    for x, y, name in zip(mean_df['放銃率'], mean_df['アガリ率'], mean_df.index):
        plt.text(x, y, name)
    st.pyplot(fig)

    st.header('平均打点vs放銃平均打点')
    fig,ax = plt.subplots(figsize=(8,8))
    plt.grid()
    sns.scatterplot(data=mean_df,x = '放銃平均打点',y='平均打点',hue='チーム')
    for x, y, name in zip(mean_df['放銃平均打点'], mean_df['平均打点'], mean_df.index):
        plt.text(x, y, name)
    st.pyplot(fig)
    
    st.header('リーチ率vs副露率')
    fig,ax = plt.subplots(figsize=(8,8))
    plt.grid()
    sns.scatterplot(data=mean_df,x = '副露率',y='リーチ率',hue='チーム')
    for x, y, name in zip(mean_df['副露率'], mean_df['リーチ率'], mean_df.index):
        plt.text(x, y, name)
    st.pyplot(fig)
    

