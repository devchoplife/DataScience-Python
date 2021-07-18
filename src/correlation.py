import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
#Correlation between engine size and price
sns.regplot(x = 'engine-sixe', y = 'price', data = df)#this plots a scatter plotto show the data  
plt.ylim(0,)#this shows a regression line to note the correlation starting at 0

#also another correlation between highway-mpg and price 
sns.regplot(x = 'highway-mpg', y = 'price', data = df)
plt.ylim(0,)