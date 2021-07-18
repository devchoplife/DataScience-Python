import seaborn as sns 

#the independent variable is x while the target variable is y and data is the name of the dataframe  
sns.regplot(x = "highway-mpg", y = "price", data = df)
plt.ylim(0,)


