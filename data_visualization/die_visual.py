from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#Create a D6
# die = Die()

# Create two D6 dice
die_1 = Die()
die_2 = Die()

#Make some rolls, and store results in a list
results = []
for roll_num in range(1000): #roll die 100 times
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results
frequencies = [] #store num of times each value rolled 
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value) #count how many times each number appears in results 
    frequencies.append(frequency) #append

#Visualize the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick':1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout (title='Results of rolling one D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')

#print(frequencies)

#print(results)

