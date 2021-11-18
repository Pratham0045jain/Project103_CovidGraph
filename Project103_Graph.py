import pandas as pd
import plotly_express as px

dataFrame = pd.read_csv('Covid_data.csv')

fig = px.scatter(dataFrame, x= 'Date', y= 'Number_of_Cases', color='country')
fig.show()