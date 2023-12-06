import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

# Use https://docs.streamlit.io/library/api-reference/layout/st.expander

df = pd.read_csv('shopping_trends_updated.csv')

st.write("""Imagine that I am trying to stock goods. I want to understand what kinds of goods I should stock, as well as when I should.
         To do so, I will use the Customer Shopping Trends Dataset from Kaggle to perform exploratory analysis.
         """)

# Pie chart
st.write("""First, let us take a look at the distribution of goods. Using a pie chart, we can visualize the percentage for each category in our store.
         Additionally, by hovering over it, we can view the gender distribution for purchases in this category.
        """)
with st.expander("test"):
    cat = round(df['Category'].value_counts()/df.shape[0],2)
    gen = df.groupby(['Gender','Category']).size()
    test = []
    for i in range(4):
        su= gen['Male'][i] + gen['Female'][i]
        test.append([gen['Male'][i], gen['Female'][i], round(gen['Male'][i]/su, 2), round(gen['Female'][i]/su, 2)])
    test[0], test[1] = test[1], test[0]
    fig = go.Figure(go.Pie(
        title="Distribution of Category",
        name = "Gender Statistics by Category",
        values = cat,
        labels = cat.index,
        text=test,
        textinfo='label+value',
        hovertemplate = "Male:%{text[0]} <br>Female:%{text[1]} <br>Male Percent Distrib:%{text[2]}<br>Female Percent Distrib:%{text[3]}"

    ))
    fig.update_layout(title='Pie Chart of Category Distribution')
    st.plotly_chart(fig)

# Box plot
fig = go.Figure()
for i, category in enumerate(df['Category'].unique()):
    df_plot = df[df['Category'] == category]
    fig.add_trace(go.Box(x=df_plot['Gender'], y=df_plot['Purchase Amount (USD)'],boxmean=True,notched=True, name=category))
#fig = go.Figure(go.Box(df, x=df['Gender'], y=''))
fig.update_layout(boxmode='group')
fig.update_layout(title='Box Plot of Purchase Amounts by Category and Gender')
fig.update_layout(yaxis_title='Purchase Amount')
st.plotly_chart(fig)

# KDE
data1 = df[df['Category'] == 'Clothing']['Age']
data2 = df[df['Category'] == 'Accessories']['Age']
data3 = df[df['Category'] == 'Outerwear']['Age']
data4 = df[df['Category'] == 'Footwear']['Age']
group_labels = ['Clothing', 'Accessories', 'Outerwear', 'Footwear']
hist_data=[data1, data2, data3, data4]
fig = ff.create_distplot(hist_data, group_labels, show_hist=False, show_rug = False)
fig.update_layout(title='Distribution of Category Purchases by Age')
fig.update_layout(xaxis_title='Age')
fig.update_layout(yaxis_title='Density')
st.plotly_chart(fig)

# Bar chart 1
itembygender=df[['Item Purchased', 'Gender']].groupby('Gender').value_counts().reset_index()
fig = px.bar(itembygender, x='Item Purchased', y='count', color='Gender')
fig.update_layout(title='Count of Items Purchased by Category and Gender')
st.plotly_chart(fig)

# Bar chart 2
byseason = df.copy()
test = byseason[['Item Purchased', 'Season']].groupby('Season').value_counts().reset_index()
fig = px.bar(test, x='Item Purchased', y='count', color='Season', barmode='group')
fig.update_layout(barmode='group', bargap=0.7,bargroupgap=0.0)
fig.update_layout(title='Count of Items Purchased by Season')
st.plotly_chart(fig)
