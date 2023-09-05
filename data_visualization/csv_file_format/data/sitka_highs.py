import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'csv_file_format/data/sitka_weather_2021_simple.csv' #assign file to variable
with open(filename) as f:  #open file and assign file to f 
    reader = csv.reader(f) #pass file to csv.reader
    header_row = next(reader) #next returns next line in file 
    #print(header_row)

#enumerate returns index and value of each item
    #for index, column_header in enumerate (header_row):
        #print(index, column_header)
    
    # Get dates and high temperatures from this file
    dates, highs = [], [] #two empty lists
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)
    #extracting and reading data
    #Get high temperatures from this file 
    #highs = []   #empty list
    #for row in reader:  #reader object continues where it left offin csv file previously
        #high = int(row[5]) #convert data to int
        #highs.append(high)
#print(highs)

# Plot the high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot
ax.set_title("Daily high temperatures - 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() #draws date label diagonally prevent overlapping
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

