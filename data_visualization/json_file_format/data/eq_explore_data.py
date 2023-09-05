import json

# Explore the structure of the data
filename = 'json_file_format/data/eq_data_1_day_m1.geojson'
with open(filename) as f:
    all_eq_data = json.load(f) #store entire set of data, json.load converts data into readable format for python


all_eq_dicts = all_eq_data['features']
#print(len(all_eq_dicts))

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    #magnitude stored in properties section under key 'mag'
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag) #add to list
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])

   # readable_file = 'json_file_format/data/readable_eq_data.geojson'
    #with open(readable_file, 'w') as f:
        #indent to match data's structure
       # json.dump(all_eq_data, f, indent=4) #takes json data object and file object and writes data to that file

