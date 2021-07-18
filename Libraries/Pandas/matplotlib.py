#MATPLOTLIB.PYPLOT FUNCTIONS 

plt.plot(x_axis, y_axis) #straight line graph 
plt.show() #to show the plots 
plt.xlabel()
plt.ylabel()
plt.yticks([], #to define the values on the y axis
            []) #to define the display names 
plt.scatter(x_axis, y_axis) #scatter plots 
plt.hist(values, bins = n) # to plot an histogram to show distrivution of data 
plt.title()
plt.fill_between(x_axis, y_axis, fill_start_origin, color = '')#a fill line chart 
plt.pcolor(df_pivot, cmap = "RdBu")#plots a heat map to show the values in the pivot table wuth color scheme red and blue 
plt.colorbar()#this shows the colorbar 
plt.ylim(origin, end)# it is a regression line and can be used together with scatter plot to show correlation between variables 
