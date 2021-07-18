import pandas as pd 

#we want to lool at the correlation between horsepower and car price 
#Scipy is used for this purpose 
pearson_coef, pvalue = stats.pearsonr(df["horsepower", df["price"]])
#the result will be the correlation coefficient and the p value 

#We can also create a correlation heatmap
plt.pcolor (pearson_coef, pvalue, cmap='RdBu')
plt.colorbar()
plt.show()
