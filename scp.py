import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

lists = pd.read_html('https://m-league.jp/stats')
img_dir = 'image'
df = pd.DataFrame()

teams = ['drivens','EX','sakura','konami','abemas','sega_summy','raiden','u-next']
teams_semi = ['EX','sakura','konami','abemas','sega_summy','u-next']
teams_final = ['sakura','konami','abemas','sega_summy']
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
df.to_csv('data/MLeague_stats.csv')
