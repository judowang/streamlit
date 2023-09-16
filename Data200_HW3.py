import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('Fish.csv', usecols=['Length1','Length2','Length3'])
fig, ax = plt.subplots()
ax.plot(df)
ax.title.set_text('Length1 vs Length2 vs Length3')
ax.set_xlabel('Fish Index')
ax.set_ylabel('Length')
ax.legend(['Length1','Length2','Length3'], loc="upper left")

st.pyplot(fig)