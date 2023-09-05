from pathlib import Path 

import json
#from plotly.graph_objs import Scattergeo, Layout
#from plotly import offline

import plotly.express as px


# Explore the structure of the data
#filename = 'json_file_format/data/eq_data_1_day_m1.geojson'
#filename = 'json_file_format/data/eq_data_30_day_m1.geojson'
#with open(filename) as f:
   # all_eq_data = json.load(f) #store entire set of data, json.load converts data into readable format for python

# Read data as a string and convert to python object 
path = Path ('data_visualization/json_file_format/data/eq_data_30_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

all_eq_dicts = all_eq_data['features']
#print(len(all_eq_dicts))

#mags, lons, lats, hover_texts = [], [], [], []
mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    #magnitude stored in properties section under key 'mag'
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    #title = eq_dict['properties']['title']
    eq_title = eq_dict['properties']['title']
    mags.append(mag) #add to list
    lons.append(lon)
    lats.append(lat)
    #hover_texts.append(title)
    eq_titles.append(eq_title)

# Map the earthquakes
#Scattergeo overlay a scatter plot of geographic data on a map
#data = [Scattergeo(lon=lons, lat=lats)]
#data = [{
    #'type': 'scattergeo',
    #'lon' : lons,
    #'lat' : lats,
    #'text': hover_texts,
    #modifying markker's appearance
    #'marker': {
        #'size': [5*mag for mag in mags],
       # 'color': mags,
        #'colorscale': 'Viridis', #tells plotly which range of colors to use
        #'reversescale': True,
        #'colorbar': {'title': 'Magnitude'},
    #},
    #}]
#my_layout = Layout(title='Global Earthquakes') #give chart title

#fig = {'data': data, 'layout': my_layout}
#offline.plot(fig, filename='global_earthquakes.html') #pass fig to plot with descriptive filename

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
        color=mags,
        color_continuous_scale='Viridis',
        labels={'color':'Magnitude'},
        projection='natural earth',
        hover_name=eq_titles,
    )
fig.show()
