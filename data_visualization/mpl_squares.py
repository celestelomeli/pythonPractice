import matplotlib.pyplot as plt #alias pyplot = plt
# pyplot module contains a number of functions that generate charts and plots

# list with data
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
# subplots f(x) generates one or more plots in same figure
fig, ax = plt.subplots() #fig represents entire figure/collection of plots generated

# ax represents single plot in figure 
ax.plot(input_values, squares, linewidth=3) #plot method tries to plot data in meaningful way
#linewidth controls thickness of line 
# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24) #sets title for chart 
ax.set_xlabel("Value", fontsize=14) # set title for each axes
ax.set_ylabel("Square of Value", fontsize=14)

# Set size/style of tick labels
ax.tick_params(axis='both', labelsize=14)
  


# open viewer and diplay plot
plt.show()