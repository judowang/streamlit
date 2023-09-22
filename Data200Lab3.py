import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('mountain_flowers.csv')

fig, ax = plt.subplots()

df.groupby(['name'])[['petal_length','petal_width']].mean().plot.bar(ax=ax)

ax.set_xlabel('Name')
ax.set_ylabel('Measurements')
ax.set_title('Average Petal Length and Width by Species')
plt.xticks(rotation=45)
st.pyplot(fig)

st.write('Dataframe:')

st.write(df)