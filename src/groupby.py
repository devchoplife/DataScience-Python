import pandas as pd
import matplotlib.pyplot as plt 

df_test = df(['drive-wheels', 'body-style', 'price'])#first pick out all the columns you want to group
df_grp = df_test.groupby(['drive-wheels', 'body-style'].as_index = False).mean()
#the above code groups the body style and drive wheels according to the average price
#as_index as false means py will assign index number but as true thefirst row will be the index number 

#to create pivots
df_pivot = df_grp.pivot(index = 'drive-wheels', columns = 'body-style')
#index is the rows while columns is the columns and the price will be displayed as values
#to create a heat map based on the pivot table 

plt.pcolor(df_pivot, cmap = 'RdBu')#cmap is the cplor scheme. in this case it is the red blue color scheme
plt.colorbar()#responsible for the deep or light colours based on the average prices
plt.show()# a heat map visualises the data on the pivot table
