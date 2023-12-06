import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff


df = pd.read_csv('shopping_trends_updated.csv')

# short intro

st.write("""Imagine that I am trying to stock goods. I want to understand what kinds of goods I should stock, as well as when I should.
         To do so, I will use the Customer Shopping Trends Dataset from Kaggle to perform exploratory analysis.
         """)

# Pie chart
st.write("""First, let us take a look at the distribution of goods. Using a pie chart, we can visualize the percentage for each category in our store.
         Additionally, by hovering over it, we can view the gender distribution for purchases in this category. With this information, we may be able to determine
         what goods to prioritize. In addition, by viewing the gender demographic, we may be able to cater our selection better.
        """)
with st.expander("Pie Chart"):
    cat = round(df['Category'].value_counts()/df.shape[0],2)  # Get the percentage distribution in decimal
    gen = df.groupby(['Gender','Category']).size()            # Used for male/female distribution
    test = []
    for i in range(4):
        su= gen['Male'][i] + gen['Female'][i]
        test.append([gen['Male'][i], gen['Female'][i], round(gen['Male'][i]/su, 2), round(gen['Female'][i]/su, 2)])    # Setting up new hover text
    test[0], test[1] = test[1], test[0]
    fig = go.Figure(go.Pie(
        title="Distribution of Category",
        name = "Gender Statistics by Category",
        values = cat,
        labels = cat.index,
        text=test,
        textinfo='label+value',
        hovertemplate = "Male:%{text[0]} <br>Female:%{text[1]} <br>Male Percent Distrib:%{text[2]}<br>Female Percent Distrib:%{text[3]}"  # hover text

    ))
    fig.update_layout(title='Pie Chart of Category Distribution')
    st.plotly_chart(fig)

# Box plot
st.write("""Next, we can use a box plot to view purchase amounts in USD per gender by category. This gives us lots of information about the spending habits for each gender.
         Additionally, this information builds upon the gender demographic from the previous chart by allowing us to determine if certain goods should be prioritized more.
         For example, if less woman have purchased clothing than men, but have spent significantly more on them, then that gives us the information to say that maybe we should
         try to provide more options for women to make a profit. However, either due to poor data or incomplete data, the purchase amounts between genders are all roughly the same.
         """)
with st.expander("Box Plot"):
    fig = go.Figure()
    for i, category in enumerate(df['Category'].unique()):
        df_plot = df[df['Category'] == category]
        fig.add_trace(go.Box(x=df_plot['Gender'], y=df_plot['Purchase Amount (USD)'],boxmean=True,notched=True, name=category)) # Have all box plots on same chart
    #fig = go.Figure(go.Box(df, x=df['Gender'], y=''))
    fig.update_layout(boxmode='group')
    fig.update_layout(title='Box Plot of Purchase Amounts by Category and Gender')
    fig.update_layout(yaxis_title='Purchase Amount')
    st.plotly_chart(fig)

# KDE
st.write("""
        Now, we will look past gender and analyze age distribution by category. Using a KDE, we can visualize the distribution of ages per category in order to determine the types of items to stock.
         In our case, for example, we notice that younger people purchase accessories and clothing more often while older people purchase outerwear and footwear more often.
         With this in mind, we are able to determine what sort of styles we can aim to stock.
         """)
with st.expander("KDE Plot"):
    data1 = df[df['Category'] == 'Clothing']['Age']             # plotly figure factory kde is based on individual (so I need to make x,y pairs)
    data2 = df[df['Category'] == 'Accessories']['Age']
    data3 = df[df['Category'] == 'Outerwear']['Age']
    data4 = df[df['Category'] == 'Footwear']['Age']
    group_labels = ['Clothing', 'Accessories', 'Outerwear', 'Footwear']
    hist_data=[data1, data2, data3, data4]
    fig = ff.create_distplot(hist_data, group_labels, show_hist=False, show_rug = False) # Due to this, the area under the curve for each is = 1 instead of all of them summed = 1
    fig.update_layout(title='Distribution of Category Purchases by Age')
    fig.update_layout(xaxis_title='Age')
    fig.update_layout(yaxis_title='Density')
    st.plotly_chart(fig)

# Bar chart 1
st.write("""
        Next, we will again expand on gender distribution. By using a stacked bar chart, we can visualize the count of each gender for purchases made on a specific item.
         Surprisingly, men have higher counts across all items, but this could simply be because of the data itself. Regardless, we can use this information to stock items of a certain style.
         """)
with st.expander("Stacked Bar Chart"):
    itembygender=df[['Item Purchased', 'Gender']].groupby('Gender').value_counts().reset_index()  # Grouping items purchased by gender
    fig = px.bar(itembygender, x='Item Purchased', y='count', color='Gender')      # By default is stacked
    fig.update_layout(title='Count of Items Purchased by Category and Gender')
    st.plotly_chart(fig)

# Bar chart 2
st.write("""
        Finally, we will use another bar chart in order to visualize item purchases by season. It may be difficult to see, but the important thing to focus on is which bar
         is the highest per category. This allows us to change our item selection based on the season. For example, jackets seem to be sold the most in the Fall, so our store
         can stock more jackets during that time. Additionally, this helps us decide the kind of jacket we would like to sell (thick v thin, waterproof v not, etc.).
         """)
with st.expander("Grouped Bar Chart"):
    byseason = df.copy()
    test = byseason[['Item Purchased', 'Season']].groupby('Season').value_counts().reset_index() # Grouping items purchased by season
    fig = px.bar(test, x='Item Purchased', y='count', color='Season', barmode='group')           # Changing to grouped mode, so each item has its season bars side by side
    fig.update_layout(barmode='group', bargap=0.7,bargroupgap=0.0)                              # Changing the gap between each item to make it a little more visible
    fig.update_layout(title='Count of Items Purchased by Season')
    st.plotly_chart(fig)
