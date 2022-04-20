#!/usr/bin/env python
# coding: utf-8

# In[56]:


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
        switch_btn.text("Mリーグデータレポート");
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

# In[57]:


import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[58]:


lists = pd.read_html('https://m-league.jp/stats/?season=L001_S011')
img_dir = 'image'
df = pd.DataFrame()
teams = ['drivens','EX','sakura','konami','abemas','sega_summy','raiden','u-next']
teams_semi = ['EX','sakura','konami','abemas','sega_summy','u-next']
j = 0
j = 0
for i in lists:
    data = i
    data = data.T
    data.columns = data.iloc[0]
    data = data[1:]
    data['チーム'] = teams_semi[j]
    j+=1
    df = pd.concat([df,data])
df.to_csv('data/MLeague_stats' + datetime.date.today().strftime('%Y-%m-%d') + '.csv')


# # 概要
# Mリーグセミファイナルが終わりました。  
# 公式サイトではセミファイナルが終わった段階でデータがでましたので、  
# 今回のMリーグセミファイナルのスタッツを見ていきたいと思います。  
# 最終戦も白熱した戦いが繰り広げ一時は奇跡が起きるかもしれないとも思わせる展開でした。  
# 最終戦までどこのチームがファイナルへ進めるか分からなかったですね。  
# 今週１週間の間を挟み、４月１８日よりファイナルが始まります。  
# Mリーグ２０２１はどこが優勝するのか！？

# # 目次:
# * [1. Mリーガ成績表](#1)
# * [2.試合数](#2)
# * [3.チーム順位 ](#3)
# * [4.ベストスコア](#4)
# * [5.順位回数](#5)
# * [6.アガリ率とトップ率](#6)
# * [7.平均打点と放銃平均打点](#7)
# * [8.さいごに](#8)

# In[59]:


print('データ取得日：'+ datetime.date.today().strftime('%Y/%m/%d'))


# # 1. Mリーガ成績表 <a class="anchor" id="1"></a>
# セミファイナル最もポイントを稼いだ選手は堀選手でした。  
# 158.3ポイントとトップ3回でサクラナイツを１位にに押し上げました。  
# セミファイナル２位の個人ポイントは岡田選手です。  
# セミファイナルサクラナイツが躍進しました。  
# 岡田選手はレギュラーシーズン苦しい麻雀をし続けられましたが、  
# セミファイナルは1着2回、2着1回と大活躍です。  
# 個人ポイント３位は小林選手です。  
# レギュラーシーズントップでセミファイナルへ臨みましたが、  
# 瑞原選手の大ブレーキ、個人レギュラーシーズントップがまさかのセミファイナルではワースト１位。  
# 麻雀の怖さを感じました。  
# 意外にもワースト２位は多井選手です。  
# 短期決戦のため、一時的なマイナスがどうしても影響してしまう難しさがありますね。  
# ただ、abemasは持ち前の安定感でチームとしてはトータルで３位にまとめてきました。  
# この安定感の強さはabemasの良いところが出たセミファイナルでした。

# In[60]:


df.sort_values('ポイント',ascending=False)


# In[61]:


df[['ポイント']].sort_values('ポイント',ascending=True).plot(kind='barh',figsize=(8,8),color='g')
plt.grid()
plt.savefig(img_dir + '/player_point.png')


# # 2. 試合数<a class="anchor" id="2"></a>
# セミファイナルの出場数は勝又選手が最多で8試合です。  
# セミファイナルの試合数の半分に出場しています。  
# だいたい4試合〜5試合の出場ですね。  
# 続いて多いのが小林選手の6試合でした。  

# In[62]:


df['試合数'].plot(kind='bar',figsize=(8,5))
plt.ylabel('試合数')
plt.savefig(img_dir + '/game.png')


# # 3.チーム順位 <a class="anchor" id="3"></a>
# セミファイナルのみの成績順位を表します。  
# 明暗が別れたのはサクラナイツとパイレーツです。   
# パイレーツは−１８４．２とレギュラーシーズンの１位通過も敗退になってしまいました。  
# 特に今シーズンはポイント差がない中での戦いでしたので、  
# 4着回数が最も多かったのがそのまま順位に響いた結果となりました。

# In[63]:


mdf = df[['試合数','チーム', '総局数', 'ポイント', '1位', '2位', '3位', '4位']].groupby('チーム').sum()


# In[64]:


mdf[['試合数', '総局数', 'ポイント', '1位', '2位', '3位', '4位']].sort_values('ポイント',ascending=False)


# In[65]:


mdf[['ポイント']].sort_values('ポイント').plot(kind='barh',color = 'orange')
plt.grid()
plt.savefig(img_dir + '/team_point.png')


# # 4. ベストスコア <a class="anchor" id="4"></a>
# セミファイナルのベストスコアで注目はabemasの４０７００点。  
# この点数を見る限り、敗退していてもおかしくないのですが、ポイントを稼げない中でもポイントを減らさない戦いができていることがとても強いです。  
# ファイナルまでは４位以内に入れば最低限良いので、負けない麻雀でファイナルへ進めます。  
# しかし、ファイナルは１位にならないといけないので、リスクをとらなければなりません。  
# ファイナルは１位を取るためにどのように麻雀を打ってくるのか注目です。

# In[66]:


df[['チーム','ベストスコア']].groupby('チーム').max().sort_values('ベストスコア',ascending = False)


# In[67]:


df[['チーム','ベストスコア']].groupby('チーム').max().plot(kind='bar',color='lime',figsize=(7,5))
plt.savefig(img_dir + '/best_score.png')


# # 5. 順位回数 <a class="anchor" id="5"></a>
# abemasの２着の多さが際立っています。  
# パイレーツは3着、4着が多くなってしまいました。  
# 2着がないのも、3着、4着に流れてしまった可能性があります。  
# EX風林火山は成績では悪くはないのですが、セミファイナル開始地点ではセガサミーとほぼ同じポイントでのスタートで、  
# 4着の回数でポイントが最後厳しくなりました。  

# In[68]:


mdf[['1位', '2位', '3位', '4位']].plot(kind='bar',figsize=(7,5))
plt.savefig(img_dir + '/rank.png')


# # 6. アガリ率と放銃率 <a class="anchor" id="6"></a>
# 放銃率とアガリ率のが共にトップのサクラナイツ。  
# セミファイナルではハイリスク・ハイリターンな結果になっています。  
# 短期決戦では１位をとらなければ始まらないので、放銃率が高くともアガリを目指さなければいけません。  
# このリスクをとって良い結果になりました。

# In[69]:


fig,ax = plt.subplots(figsize=(5,5))
mean_df = df[['チーム','ベストスコア','トップ率', '連対率','平均打点','放銃平均打点',
       'ラス回避率', '副露率', 'リーチ率', 'アガリ率', '放銃率']].groupby('チーム').mean()
sns.scatterplot(data=mean_df,x = '放銃率',y='アガリ率',hue='チーム')
for x, y, name in zip(mean_df['放銃率'], mean_df['アガリ率'], mean_df.index):
    plt.text(x, y, name)
plt.grid()
plt.savefig(img_dir + '/agari_houju.png')


# # 7. 平均打点と放銃平均打点 <a class="anchor" id="7"></a>
# 平均打点のトップは風林火山です。  
# それ以上にアガあれませんでした。  
# チーム雷電のときもそうでしたが、アガリ率が低すぎるとそもそも加点さればいのでポイントが稼げません。  
# セミファイナルは短期決戦ですのでこの数字はブレが大きいものになりますが、  
# その中で勝っていかなければいけない難しさがありますね。

# In[70]:


fig,ax = plt.subplots(figsize=(5,5))
sns.scatterplot(data=mean_df,x = '放銃平均打点',y='平均打点',hue='チーム')
for x, y, name in zip(mean_df['放銃平均打点'], mean_df['平均打点'], mean_df.index):
    plt.text(x, y, name)
plt.grid()
plt.savefig(img_dir + '/ave_point.png')


# # 8. さいごに <a class="anchor" id="8"></a>
# セミファイナルが終え、ついにファイナルが来週から始まります！  
# Mリーグ２０２１の優勝チームはどこか！！  
# 最後まで見守っていきたいと思います。

# In[ ]:




