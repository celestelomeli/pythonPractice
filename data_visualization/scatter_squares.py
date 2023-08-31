import matplotlib.pyplot as plt

#x_values = [1, 2, 3, 4, 5] #values to be squared
#y_values = [1, 4, 9, 16, 25] #square of each value

x_values = range(1, 1001) #numbers 1- 1000
y_values = [x**2 for x in x_values] #loop through x_values, square each number, store in y_values


plt.style.use('seaborn')
fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10) #s determines size of dots, c= color
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) #colormaps to emphasize pattern in data


# Set chart title and label axes 
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels 
ax.tick_params(axis= 'both', which='major', labelsize=14)

# Set range for each axis
# use axis method to specify range of each axis requiring 4 values(min & max values for x and y axis)
ax.axis([0, 1100, 0, 1100000])
#plt.show()

 # first arg= filename for plot image, second arg= trims extra whitespace
plt.savefig('squares_plot.png', bbox_inches='tight') 