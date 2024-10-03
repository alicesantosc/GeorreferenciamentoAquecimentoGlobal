import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px

global_temp_country= pd.read_csv('tabelas/GlobalLandTemperaturesByCountry.csv')
#global_temp_country.head()

###tirando campos nulos
global_temp_country.dropna(axis='index', how='any',subset=['AverageTemperature'], inplace=True)
#print(global_temp_country.isna().sum())
###
avg_temp = global_temp_country.groupby(['Country'])['AverageTemperature'].mean().to_frame().reset_index()

fig = px.choropleth(avg_temp, locations='Country', locationmode='country names',color='AverageTemperature')
fig.update_layout(title='Mapa Colorido de acordo com a temperatura')
fig.show()

global_temp = pd.read_csv('tabelas/GlobalTemperatures.csv')
#print(global_temp.head())

def fetch_year(date):
    return date.split('-')[0]
global_temp['years']=global_temp['dt'].apply(fetch_year)
global_temp.head()


data = global_temp.groupby('years').agg({'LandAverageTemperature':'mean','LandAverageTemperatureUncertainty':'mean'}).reset_index()
data['Uncertainty Top'] = data['LandAverageTemperature'] + data['LandAverageTemperatureUncertainty']
data['Uncertainty Bottom'] = data['LandAverageTemperature'] - data['LandAverageTemperatureUncertainty']
print(data.head())
print(data.columns)
fig2 = px.line(data,x='years', y=['LandAverageTemperature','LandAverageTemperatureUncertainty','Uncertainty Top', 'Uncertainty Bottom'],title='Temperatura media no Mundo')
fig2.show()