import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


df = pd.read_csv('Fish.csv')
option = st.selectbox('Which graph would you like to view?',
('All','Line','Boxplot','Histogram','Scatter Plot','Bar'))

def linePlot():
   fig1, ax1 = plt.subplots()
   ax1.plot(df[['Length1','Length2','Length3']])
   ax1.title.set_text('Length1 vs Length2 vs Length3')
   ax1.set_xlabel('Fish Index')
   ax1.set_ylabel('Length')
   ax1.legend(['Length1','Length2','Length3'], loc="upper left")
   st.pyplot(fig1)

def boxPlot():
   fig2, ax2 = plt.subplots()
   df.boxplot(column='Weight', by='Species', ax=ax2)
   ax2.set_ylabel('Weight')
   st.pyplot(fig2)

def histPlot():
   fig3,ax3 = plt.subplots()
   df['Species'].value_counts().plot.bar(ax=ax3)
   ax3.set_title('Count of Species')
   ax3.set_ylabel('Count')
   plt.xticks(rotation=45)
   st.pyplot(fig3)

def scatterPlot():
   fig4, ax4 = plt.subplots()
   df.plot.scatter(x='Length1',y='Weight', ax=ax4)
   ax4.set_title('Correlation of Length1 and Weight')
   st.pyplot(fig4)

def barPlot():
   fig5, ax5 = plt.subplots()
   df.groupby(['Species'])[['Length1','Length2','Length3','Width','Height']].mean().plot.bar(ax=ax5)
   ax5.set_title('Average Lengths, Heights, and Widths by Species')
   plt.xticks(rotation=45)
   ax5.set_ylabel('Measurements')
   st.pyplot(fig5)
  

if option == 'All':
   linePlot()
   boxPlot()
   histPlot()
   scatterPlot()
   barPlot()
elif option=='Line':
   linePlot()
elif option=='Boxplot':
   boxPlot()
elif option=='Histogram':
   histPlot()
elif option =='Scatter Plot':
   scatterPlot()
elif option=='Bar':
   barPlot()

