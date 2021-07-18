import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

#still baed on the car scenario
drive_wheel_counts = df["drive-wheels"].value_counts()#counts the number of drive wheels in the column 

#Change the cpl;umn name for more readability 
#remeber the dataframe is drive_wheel_counts
drive_wheel_counts.rename (columns = ['drive-wheels': 'value-counts'], inplace = True)#
#The above code is to rename a colum in the dataframe 
drive_wheel_counts.index.name = 'drive-wheels'# to assign the index name 

#to plot a boxplot for numeric data 
sns.boxplot(x = "drive-wheels", y = "price", data = df)#df is the dataframe to extract the data from

x = ["engine-size"]
y = ["price"]
plt.scatter(x, y)
plt.title("Scatter plot of engine size vs price")
plt.xlabel("engine size")
plt.ylabel("Price")
plt.show()