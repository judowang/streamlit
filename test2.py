import pandas as pd
import scipy
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv('shopping_trends_updated.csv')
#display(df)
cat = round(df['Category'].value_counts()/df.shape[0],2)
gen = df.groupby(['Gender','Category']).size()
test = []
for i in range(4):
    su= gen['Male'][i] + gen['Female'][i]
    test.append([gen['Male'][i], gen['Female'][i], round(gen['Male'][i]/su, 2), round(gen['Female'][i]/su, 2)])
test[0], test[1] = test[1], test[0]
# Hover Text
# This chart shows the distribution of transactions by category. From this, we can see the most common categories purchased are.
# Additionally, through the use of hover text, the chart shows the distribution of male/female buyers by category.
# Surprisingly, males seem to have more transactions across all categories.
fig = go.Figure(go.Pie(
    title="Distribution of Category",
    name = "Gender Statistics by Category",
    values = cat,
    labels = cat.index,
    text=test,
    textinfo='label+value',
    hovertemplate = "Male:%{text[0]} <br>Female:%{text[1]} <br>Male Percent Distrib:%{text[2]}<br>Female Percent Distrib:%{text[3]}"

))
fig.show();
#fig = px.box(df, x='Gender', y='Purchase Amount (USD)', color='Category')
fig = go.Figure()
for i, category in enumerate(df['Category'].unique()):
    df_plot = df[df['Category'] == category]
    fig.add_trace(go.Box(x=df_plot['Gender'], y=df_plot['Purchase Amount (USD)'],boxmean=True,notched=True, name=category))
#fig = go.Figure(go.Box(df, x=df['Gender'], y=''))
fig.update_layout(boxmode='group')
fig.update_layout(title='Box Plot of Purchase Amounts by Category and Gender')
fig.show();
# Distribution curve (kde) of the above
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

fig.show();
itembygender=df[['Item Purchased', 'Gender']].groupby('Gender').value_counts().reset_index()
px.bar(itembygender, x='Item Purchased', y='count', color='Gender')
byseason = df.copy()
test = byseason[['Item Purchased', 'Season']].groupby('Season').value_counts().reset_index()
fig = px.bar(test, x='Item Purchased', y='count', color='Season', barmode='group')
fig.update_layout(barmode='group', bargap=0.7,bargroupgap=0.0)
fig.show();
