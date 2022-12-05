#!/usr/bin/env python
# coding: utf-8

# In[71]:


import pandas as pd
import datetime
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import streamlit as st
import streamlit.components.v1 as stc
import numpy as np
# %matplotlib inline

fname = 'data/MLeague_stats.csv'

def PlayerInfo(player):
    if player == '鈴木 たろう':
        st.text('書籍')
        st.markdown('<a href = "https://amzn.to/3VwgK2i">最強プロ鈴木たろうの 迷わず強くなる麻雀</a>',unsafe_allow_html=True)
        st.markdown('<a href = "https://amzn.to/3B8D1v6">ゼウスの選択 デジタル麻雀最終形 (マイナビ麻雀BOOKS) 単行本</a>',unsafe_allow_html=True)
        st.text('YouTube')
        st.markdown('<a href = "https://www.youtube.com/channel/UC6a6NvU9sgTHniE5h10i6rw">鈴木たろうちゃんねる</a>',unsafe_allow_html=True)

    if player == '園田 賢':
        st.text('書籍')
        st.markdown('<a href = "https://amzn.to/3Y1rgR8">麻雀のネクストレベルの扉を開く 魔術の麻雀</a>',unsafe_allow_html=True)
        
    if player == '村上 淳':
        st.text('書籍')
        st.markdown('<a href = "https://amzn.to/3ixwELn">トッププロに聞いた 麻雀「読み」の神髄</a>',unsafe_allow_html=True)
        st.markdown('<a href = "https://amzn.to/3iF9sLn">麻雀・手牌読みハンドブック【近代麻雀付録小冊子シリーズ】</a>',unsafe_allow_html=True)
        
    if player == '丸山 奏子':
        st.text('グッズ')
        st.markdown('<a href = "https://amzn.to/3VEz6i0">最高位戦日本プロ麻雀協会 オフィシャルグッズ アクリルキーホルダー</a>',unsafe_allow_html=True)
         
    if player == '二階堂 亜樹':
        st.text('書籍')
        st.markdown('<a href = "https://amzn.to/3HfpvcS">二階堂亜樹の勝てる麻雀の基本</a>',unsafe_allow_html=True)
        st.markdown('<a href = "https://amzn.to/3uqer52">誰でもすぐ上達! 二階堂亜樹のひと目の何切る</a>',unsafe_allow_html=True)
        st.markdown('<a href = "https://amzn.to/3VSqq7b">二階堂亜樹の勝てる麻雀 守りの基本</a>',unsafe_allow_html=True)
        st.markdown('<a href = "https://amzn.to/3iFC6f5">麻雀を始めたい人のために</a>',unsafe_allow_html=True)

    if player == '勝又 健志':
        st.text('書籍')
        st.markdown('<a href = "https://amzn.to/3VM6UsQ">麻雀IQ220の選択 (近代麻雀戦術シリーズ) </a>',unsafe_allow_html=True)
        st.markdown('<a href = "https://amzn.to/3XS58Zn">麻雀IQ220の決断【近代麻雀付録小冊子シリーズ】</a>',unsafe_allow_html=True)
    if player == '松ヶ瀬 隆弥':
        st.text('YouTube')
        st.markdown('<a href = "https://www.youtube.com/channel/UCYHMQp5n9f_GHKnV8DnYfmw">私立松ヶ瀬学園</a>',unsafe_allow_html=True)
        
    if player == '二階堂 瑠美':
        st.text('書籍')
        st.markdown('<a href = "https://amzn.to/3VzuNnR">いきあたりガッポリ 2013実戦編</a>',unsafe_allow_html=True)

    if player == '内川 幸太郎':
        st.text('書籍')
        st.markdown('<a href = "https://amzn.to/3VStGzr">東海オンエア虫眼鏡×Mリーガー内川幸太郎 勝てる麻雀をわかりやすく教えてください!</a>',unsafe_allow_html=True)
        st.markdown('<a href = "https://amzn.to/3gXtpN0">現代麻雀の絶対手順 (マイナビ麻雀BOOKS)</a>',unsafe_allow_html=True)

    if player == '岡田 紗佳':
        st.text('写真集')
        st.markdown('<a href = "https://amzn.to/3Y0p10n">おかぴーの森へようこそ 週刊ポストデジタル写真集</a>',unsafe_allow_html=True)
        st.markdown('<a href = "https://amzn.to/3iCKz2R">「寝かせないで」ＳＰＡ！グラビアン魂デジタル写真集 (ＳＰＡ！ＢＯＯＫＳ)</a>',unsafe_allow_html=True)
        st.markdown('<a href = "https://amzn.to/3F0vrnj">secret trip 【シークレットトリップ】</a>',unsafe_allow_html=True)

    if player == '滝沢 和典':
        st.text('書籍')
        st.markdown('<a href = "https://amzn.to/3VA3qdh">麻雀 読みの技術 (日本プロ麻雀連盟BOOKS)</a>',unsafe_allow_html=True)
        st.markdown('<a href = "https://amzn.to/3P9v9zm">滝沢の麻雀 勝利への絶対条件 (マイコミ麻雀BOOKS)</a>',unsafe_allow_html=True)
        st.markdown('<a href = "https://amzn.to/3FsSPeJ">滝沢和典の麻雀読みの公式 (日本プロ麻雀連盟BOOKS)</a>',unsafe_allow_html=True)
    
    if player == '佐々木 寿人':
        st.text('書籍')
        st.markdown('<a href = "https://amzn.to/3ForvOF">進化した「超攻撃」スタイル! 魔王の麻雀</a>',unsafe_allow_html=True)
        st.markdown('<a href = "https://amzn.to/3iwe329">ヒサトノート 強者のメンタル強化塾 (近代麻雀戦術シリーズ)</a>',unsafe_allow_html=True)
        
    if player == '高宮 まり':
        st.text('DVD')
        st.markdown('<a href = "https://amzn.to/3XYl783">幸福論 ［DVD］</a>',unsafe_allow_html=True)
        st.markdown('<a href = "https://amzn.to/3iz2eIG">A Day In The Life [DVD]</a>',unsafe_allow_html=True)
        st.text('ダーツ')
        st.markdown('<a href = "https://amzn.to/3VPUT5H">DYNASTY ダイナスティー collaboration LADYBERSERK レディーベルセルク 2BA 高宮まりモデル ダーツ バレル ダーツセット</a>',unsafe_allow_html=True)
        st.text('写真集')
        st.markdown('<a href = "https://amzn.to/3F4Vs56">牌×牌more 週刊ポストデジタル写真集</a>',unsafe_allow_html=True)
        
    if player == '伊達 朱里紗':
        st.text('主演作品')
        st.markdown('<a href = "https://amzn.to/3P0HFkm">ヲタクに恋は難しい (完全生産限定版)(全4巻セット/発売日順次お届け)[Blu-ray]</a>',unsafe_allow_html=True)
        
    if player == '白鳥 翔':
        st.text('書籍')
        st.markdown('<a href = "https://amzn.to/3H7Wxf7">トッププロが教える 最強の麻雀押し引き理論</a>',unsafe_allow_html=True)
        
    if player == '松本 吉弘':
        st.text('書籍')
        st.markdown('<a href = "https://amzn.to/3upJM81">初代Mリーガー松本のベストバランス麻雀 (マイナビ麻雀BOOKS)</a>',unsafe_allow_html=True)
        
    if player == '日向 藍子':
        st.text('Twitter')
        st.markdown('<a href = "https://twitter.com/hinaai0924">Twitterアカウント：日向藍子</a>',unsafe_allow_html=True)

    if player == '魚谷 侑未':
        st.text('書籍')
        st.markdown('<a href = "https://amzn.to/3P3pcUD">改訂版 ゆーみんの現代麻雀が最速で強くなる本</a>',unsafe_allow_html=True)
        st.markdown('<a href = "https://amzn.to/3iGcMpD">麻雀が強くなるための心と技術 (近代麻雀戦術シリーズ)</a>',unsafe_allow_html=True)
        st.markdown('<a href = "https://amzn.to/3FuSgBi">ゆーみんの現代麻雀が最速で強くなる本</a>',unsafe_allow_html=True)
        
    if player == '近藤 誠一':
        st.text('書籍')
        st.markdown('<a href = "https://amzn.to/3VyVnxw">麻雀 理論と直感力の使い方 (近代麻雀戦術シリーズ)</a>',unsafe_allow_html=True)
        st.markdown('<a href = "https://amzn.to/3uoglTO">最強雀士が語るデジタルの向こう側 大きく打ち、大きく勝つ麻雀 (マイナビ麻雀BOOKS)</a>',unsafe_allow_html=True)
        
    if player == '茅森 早香':
        st.text('グッズ')
        st.markdown('<a href = "https://amzn.to/3VAbhaR">最高位戦日本プロ麻雀協会 オフィシャルグッズ エコバッグ</a>',unsafe_allow_html=True)

    if player == '東城 りお':
        st.text('DVD')
        st.markdown('<a href = "https://amzn.to/3F3wByy">Rio TIME! [DVD]</a>',unsafe_allow_html=True)

    if player == '萩原 聖人':
        st.text('書籍')
        st.markdown('<a href = "https://amzn.to/3FsMqjH">麻雀 逆境の凌ぎ方 (近代麻雀戦術シリーズ)</a>',unsafe_allow_html=True)

    if player == '瀬戸熊 直樹':
        st.text('書籍')
        st.markdown('<a href = "https://amzn.to/3XQHa0m">麻雀 アガリの技術 (日本プロ麻雀連盟BOOKS)</a>',unsafe_allow_html=True)

    if player == '黒沢 咲':
        st.text('書籍')
        st.markdown('<a href = "https://amzn.to/3P4y2Ba">黒沢咲の 鳴かずに勝つ! セレブ麻雀 (Mahjong Books)</a>',unsafe_allow_html=True)
        st.markdown('<a href = "https://amzn.to/3XQHufA">渚のリーチ!</a>',unsafe_allow_html=True)
        
    if player == '本田 朋広':
        st.text('DVD')
        st.markdown('<a href = "https://amzn.to/3VwGufh">麻雀最強戦2022 #4ミスター麻雀カップ上巻 [DVD]</a>',unsafe_allow_html=True)

    if player == '小林 剛':
        st.text('書籍')
        st.markdown('<a href = "https://amzn.to/3F4cQXJ">コバゴー式　麻雀“早覚え”点数計算マスタードリル (I・P・S MOOK)</a>',unsafe_allow_html=True)
        st.markdown('<a href = "https://amzn.to/3umZLUt">アガリ率5%アップ何切る (近代麻雀 戦術シリーズ)</a>',unsafe_allow_html=True)
        st.markdown('<a href = "https://amzn.to/3uqJiyp">スーパーデジタル麻雀 (近代麻雀戦術シリーズ)</a>',unsafe_allow_html=True)
    
    if player == '瑞原 明奈':
        st.text('書籍')
        st.markdown('<a href = "https://amzn.to/3Fph7Gp">瑞原明奈のロジカル麻雀入門 (マイナビ麻雀BOOKS)</a>',unsafe_allow_html=True)
        
    if player == '鈴木 優':
        st.text('書籍')
        st.markdown('<a href = "https://amzn.to/3Vz0QEy">フルカラー改訂版 1秒で見抜く麻雀心理術 (近代麻雀戦術シリーズ)</a>',unsafe_allow_html=True)
        st.markdown('<a href = "https://amzn.to/3VxRybV">1秒で見抜くヤバい麻雀心理術 (近代麻雀戦術シリーズ)</a>',unsafe_allow_html=True)
    
    if player == '仲林 圭':
        st.text('YouTube')
        st.markdown('<a href = "https://www.youtube.com/channel/UCPoSb5QLf0ZcQ0C-rJYK2IQ?app=desktop">じゃがちゃんねる【仲林圭】</a>',unsafe_allow_html=True)
    
def rader_c(labels,values):

        # 多角形を閉じるためにデータの最後に最初の値を追加する。
        radar_values = np.concatenate([values, [values[0]]])
        # プロットする角度を生成する。
        angles = np.linspace(0, 2 * np.pi, len(labels) + 1, endpoint=True)
        # メモリ軸の生成
        rgrids = [0, 0.1, 0.2, 0.3, 0.4]

        fig = plt.figure(facecolor="w")
        # 極座標でaxを作成
        ax = fig.add_subplot(1, 1, 1, polar=True)
        # レーダーチャートの線を引く
        ax.plot(angles, radar_values)
        #　レーダーチャートの内側を塗りつぶす
        ax.fill(angles, radar_values, alpha=0.2)
        # 項目ラベルの表示
        ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels)
        # 円形の目盛線を消す
        ax.set_rgrids([])
        # 一番外側の円を消す
        ax.spines['polar'].set_visible(False)
        # 始点を上(北)に変更
        ax.set_theta_zero_location("N")
        # 時計回りに変更(デフォルトの逆回り)
        ax.set_theta_direction(-1)

        # 多角形の目盛線を引く
        for grid_value in rgrids:
            grid_values = [grid_value] * (len(labels)+1)
            ax.plot(angles, grid_values, color="gray",  linewidth=0.5)

        # メモリの値を表示する
        for t in rgrids:
            # xが偏角、yが絶対値でテキストの表示場所が指定される
            ax.text(x=0, y=t, s=t)

        # rの範囲を指定
        ax.set_rlim([min(rgrids), max(rgrids)])
        ax.set_title("麻雀スタイル", pad=20)
        st.pyplot(fig)        
    
if __name__ == "__main__":
    st.set_page_config(
        page_title="Mリーグ２０２２-２０２３スタッツサイト",
        page_icon="🀄️",
        initial_sidebar_state="expanded"
    )
    
    df = pd.read_csv(fname)
    df.rename(columns={'Unnamed: 0': '選手名'},inplace=True)
    df.index = df['選手名']
    df.drop('選手名',axis = 1,inplace=True)
    
    st.title('Mリーグ2022-2023スタッツサイト')
    st.write('Mリーグ選手成績データ可視化サイトです。')
    st.write('現在は2022-2023レギュラーシーズン成績を可視化しています。')
    st.markdown('<a href = "https://m-league.jp/">公式サイトはこちら</a>',unsafe_allow_html=True)
    st.markdown('<a href="https://px.a8.net/svt/ejp?a8mat=3N26CN+5YCTU+4EKC+5YJRM" rel="nofollow">MリーグはABEMAで見れます！</a><img border="0" width="1" height="1" src="https://www18.a8.net/0.gif?a8mat=3N26CN+5YCTU+4EKC+5YJRM" alt="">',unsafe_allow_html=True)
    
    tab1, tab2,tab3 = st.tabs(["個人成績", "チーム成績","選手プロフィール"])
    
    with tab1:
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
        st.header('平均アガリ率vs平均放銃率')
        fig,ax = plt.subplots(figsize=(8.0,8.0))
        plt.grid()

        sns.scatterplot(data=df,x = '放銃率',y='アガリ率',hue='チーム')
        for x, y, name in zip(df['放銃率'], df['アガリ率'], df.index):
            plt.text(x, y, name)
        st.pyplot(fig)
        
        st.header('平均打点vs平均放銃点')
        fig,ax = plt.subplots(figsize=(8,8))
        plt.grid()
        sns.scatterplot(data=df,x = '放銃平均打点',y='平均打点',hue='チーム')
        for x, y, name in zip(df['放銃平均打点'], df['平均打点'], df.index):
            plt.text(x, y, name)
        st.pyplot(fig)
        
        st.header('リーチ率vs副露率')
        fig,ax = plt.subplots(figsize=(8,8))
        plt.grid()
        sns.scatterplot(data=df,x = '副露率',y='リーチ率',hue='チーム')
        for x, y, name in zip(df['副露率'], df['リーチ率'], df.index):
            plt.text(x, y, name)
        st.pyplot(fig)
        
        st.header('試合数vs対局数')
        fig,ax = plt.subplots(figsize=(8,8))
        plt.grid()
        sns.scatterplot(data=df,x = '試合数',y='総局数',hue='チーム')
        for x, y, name in zip(df['試合数'], df['総局数'], df.index):
            plt.text(x, y, name)
        st.pyplot(fig)
        
    with tab2:
        st.header('チームポイントランキング')
        mdf = df[['試合数','チーム', '総局数', 'ポイント', '1位', '2位', '3位', '4位']].groupby('チーム').sum()
        mdf[['試合数', '総局数', 'ポイント', '1位', '2位', '3位', '4位']] = mdf[['試合数', '総局数', 'ポイント', '1位', '2位', '3位', '4位']].astype(int)
        st.table(mdf[['試合数', '総局数', 'ポイント', '1位', '2位', '3位', '4位']].sort_values('ポイント',ascending=False))
        
        arr = mdf[['試合数', '総局数', 'ポイント', '1位', '2位', '3位', '4位']].sort_values('ポイント',ascending=True)
        fig,ax = plt.subplots(figsize=(8.0, 8.0))
        ax.barh(arr.index.to_list(),arr['ポイント'].to_list(),align = 'center',color='green')
        ax.grid()
        st.pyplot(fig)

        st.header('平均アガリ率vs平均放銃率')
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
        
        st.header('平均トップ率vs平均ラス回避率')
        fig,ax = plt.subplots(figsize=(8,8))
        plt.grid()
        sns.scatterplot(data=mean_df,x = 'トップ率',y='ラス回避率',hue='チーム')
        for x, y, name in zip(mean_df['トップ率'], mean_df['ラス回避率'], mean_df.index):
            plt.text(x, y, name)
        st.pyplot(fig)
        
    with tab3:
        
        'Mリーガの個人成績、タイトル、書籍等の情報をまとめています。'
        '下から選手を選択するとMリーグ個人データが見れます。'
        
        option = st.selectbox(
                'Mリーガ選択',
                (df.index.unique())
            )

        df2 = df.drop('チーム',axis=1)
        data = df2.loc[option]
        data_l = pd.DataFrame(data)
        data_lc = pd.DataFrame(df2[['放銃平均打点','平均打点']].loc[option])
        data_r = pd.DataFrame(df2[['アガリ率','リーチ率','副露率']].loc[option])
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric('ポイント',data['ポイント'])
        with col2:
            st.metric('ベストスコア',data['ベストスコア'])
        with col3:
            st.metric('ラス回避率',data['ラス回避率'])
        
        col4,col5 = st.columns(2)
        with col4:
            st.table(data_l.style.format('{:.2f}'))
        
        with col5:
            fig,ax = plt.subplots(figsize=(8.0, 8.0))
            rader_c(data_r.index.to_list(),np.array(data_r[option].to_list()))
            ax.grid()
  
            fig,ax = plt.subplots(figsize=(8.0, 8.0))
            ax.barh(data_lc.index.to_list(),data_lc[option].to_list(),align = 'center',color='lightgreen')
            ax.grid()        
            st.pyplot(fig)

        PlayerInfo(option)

