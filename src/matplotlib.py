import matplotlib.pyplot as plt #this is for the visualisation tool matplotlib

year = [1950, 1960, 1970, 1980, 1990]
popul = [2.519, 3.692, 5.263, 6.972, 8.345]#expressed in billions

plt.plot (year, popul)#this is a line chart 
plt.show() #the plot will not be showm if this is not used because python assumes you want to add more data

plt.scatter (year, popul)#this is a scatter chart
plt.show()