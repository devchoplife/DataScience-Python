import matplotlib.pyplot as plt 

year = [1950, 1960, 1970, 1980, 1990]
population = [2.519, 3.692, 5.263, 6.972, 8.345]

year = [1800, 18550, 1900] + year
population = [1.0, 1.262, 1.650] + population#adds the new values to the existing values 

plt.plot (year, population)
plt.xlabel ('Year')
plt.ylabel ('Population')
plt.title ('World Population Data')
plt.yticks ([0, 2, 4, 6, 8, 10],  #defining the y values on the chart 
												['0', '2B', '4B', '6B', '8B', '10B'])# defining the display name of the values

