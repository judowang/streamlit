import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('mountain_flowers.csv')

st.write('This bar chart shows the average petal length and width for each flower.')

fig, ax = plt.subplots()

df.groupby(['name'])[['petal_length','petal_width']].mean().plot.bar(ax=ax)

ax.set_xlabel('Species')
ax.set_ylabel('Measurements')
ax.set_title('Average Petal Length and Width by Species')
plt.xticks(rotation=45)
st.pyplot(fig)

st.write('We note that the Colorado Lotus is the largest, followed by the bluebells, then violets.')

st.write('**Detailed Data View:**')

st.write(df)
