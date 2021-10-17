#!/usr/bin/env python
# coding: utf-8

# In[249]:


from IPython.display import HTML

HTML("""
<button id="code-show-switch-btn">スクリプトを非表示にする</button>

<script>
var code_show = true;

function switch_display_setting() {
    var switch_btn = $("#code-show-switch-btn");
    if (code_show) {
        $("div.input").hide();
        code_show = false;
        switch_btn.text("Mリーグレポート");
    }else {
        $("div.input").show();
        code_show = true;
        switch_btn.text("スクリプトを非表示にする");
    }
}

$("#code-show-switch-btn").click(switch_display_setting);
</script>
""")


# # Mリーグデータレポート

# In[250]:


import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[251]:


lists = pd.read_html('https://m-league.jp/stats')
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
df.to_csv('data/MLeague_stats' + datetime.date.today().strftime('%Y-%m-%d') + '.csv')


# # 目次:
# * [1. Mリーガ成績表](#1)
# * [2.試合数](#2)
# * [3.チーム順位 ](#3)
# * [4.ベストスコア](#4)
# * [5.順位回数](#5)
# * [6.アガリ率とトップ率](#6)
# * [7.平均打点と放銃平均打点](#7)
# * [8.さいごに](#8)

# In[252]:


print('データ取得日：'+ datetime.date.today().strftime('%Y/%m/%d'))


# # 1. Mリーガ成績表 <a class="anchor" id="1"></a>
# 沢崎選手が今シーズン１勝目を取りポイントを１３０として、個人ポイント成績２位に浮上しました。  
# まだ放銃を１回もしていないです。  
# どこまで放銃をしないで続くか注目です。  
# 浅倉選手が１位を取ったことで個人ポイント成績が４位です。  
# 今年のパイレーツは浅倉選手が引っ張ってくれるのか！？  

# In[253]:


df.sort_values('ポイント',ascending=False)


# # 2. 試合数<a class="anchor" id="2"></a>
# 大体2〜３試合の出場数です。  
# 伊達選手、二階堂瑠美選手、東城選手はまだ１試合とどのように起用していくか注目です。  
# 丸山選手も今シーズンは出場数を他の3人と同じくらいの２０試合くらい出れるとチームとしての厚さも増すので期待したいところです。  

# In[254]:


df['試合数'].plot(kind='bar')
plt.ylabel('試合数')


# # 3.チーム順位 <a class="anchor" id="3"></a>
# ２週目を終えて、全チーム８試合を消化しました。  
# ポイントは雷電が１２５ポイント、風林火山が102ポイントと頭ひとつ抜けた形になりました。  
# ３位から６位は３７．３ポイント差と固まっています。  
# ７位ドリブンズが−７５、８位konamiが−１０８と少し出だしにつまづいた感じです。  
# ドリブンズ、コナミはこのままズルズルいきたくないところです。  

# In[257]:


mdf = df[['試合数','チーム', '総局数', 'ポイント', '1位', '2位', '3位', '4位']].groupby('チーム').sum()


# In[258]:


mdf[['試合数', '総局数', 'ポイント', '1位', '2位', '3位', '4位']].sort_values('ポイント',ascending=False)


# In[259]:


mdf[['ポイント']].sort_values('ポイント').plot(kind='barh',color = 'orange')
plt.grid()


# # 4. ベストスコア <a class="anchor" id="4"></a>
# ベストスコアは２週目も終えたところ、konamiの５６２００がトップベストスコアをキープしています。  
# 破壊力があるチームですから、一度きっかけがあればいっきに上がってくるポテンシャルを持ってるチームです。  
# 連勝、１位２位フィニッシュで波に乗るのを期待しましょう。  
# 対して、ドリブンズはベストスコア最下位なところは得点を取れてない点で少し心配です。

# In[262]:


df[['チーム','ベストスコア']].groupby('チーム').max().sort_values('ベストスコア',ascending = False)


# In[263]:


df[['チーム','ベストスコア']].groupby('チーム').max().plot(kind='bar',color='lime',figsize=(7,5))


# # 5. 順位回数 <a class="anchor" id="5"></a>
# 順位回数を見てみると雷電の方が風林火山と比べると４位回数が１回少なく順位回数では良い成績です。  
# ポイント差では風林火山が上回っています。  
# １位、２位は互角の状態です。  
# ２週目が終わり、３位が増えたドリブンズ、なかなか勝ちきれない厳しい週となりました。  

# In[265]:


mdf[['1位', '2位', '3位', '4位']].plot(kind='bar',figsize=(7,5))


# # 6. アガリ率と放銃率 <a class="anchor" id="6"></a>
# 放銃率に大きな動きがありました。
# ドリブンズが0.17の放銃率に対して、他７チームは０．０９から０．１２の間にあります。  
# かなり大きく離れています。  
# まだ序盤のため、１週立てばまた大きく変わりますが、今週に関していえば、  
# この放銃率がドリブンズの苦しい週で７位になってしまったことの原因の一つでしょう。  
# セガサミーのアガリ率の高さはと放銃率の低さは８チーム中トップクラスです。  

# In[268]:


fig,ax = plt.subplots(figsize=(8,8))
mean_df = df[['チーム','ベストスコア','トップ率', '連対率','平均打点','放銃平均打点',
       'ラス回避率', '副露率', 'リーチ率', 'アガリ率', '放銃率']].groupby('チーム').mean()
sns.scatterplot(data=mean_df,x = '放銃率',y='アガリ率',hue='チーム')
for x, y, name in zip(mean_df['放銃率'], mean_df['アガリ率'], mean_df.index):
    plt.text(x, y, name)
plt.grid()


# # 7. 平均打点と放銃平均打点 <a class="anchor" id="7"></a>
# 打点に着目すると、打点が高く放銃打点も低いのはサクラナイツです。  
# また、１位、２位を取ったことでプラスになったu-nextは平均打点６５００弱、放銃平均打点も３５００強と２番目に低いです。  
# データ上は打点、率ともに良い数値を出しているu-nextが３週目上がってくるか期待です。  
# セガサミー、ドリブンズは放銃打点の大きさが厳しいところか。  
# 大きい振り込みがどうしても勝ちきれないところにつながっているか・・・。  

# In[269]:


fig,ax = plt.subplots(figsize=(8,8))
sns.scatterplot(data=mean_df,x = '放銃平均打点',y='平均打点',hue='チーム')
for x, y, name in zip(mean_df['放銃平均打点'], mean_df['平均打点'], mean_df.index):
    plt.text(x, y, name)
plt.grid()


# # 8. さいごに <a class="anchor" id="8"></a>
# データに大きく変動が見られる２週目でした。  
# 1位、２位が抜け出すか、７位、８位が這い上がるか注目の３週目です。

# In[ ]:




