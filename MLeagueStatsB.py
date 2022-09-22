import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import streamlit as st

if __name__ == "__main__":
	st.title('Mリーグスタッツ')
	st.write(('データ取得日：'+ datetime.date.today().strftime('%Y/%m/%d'))

	df = pd.read_csv('data/MLeague_stats2022-04-29.csv',index='選手名')

	st.dataframe(df.sort_values('ポイント',ascending=False)

