#EXPLORATORY DATA ANALYSIS TECHNIQUES
#Descriptive statistics, Groupby, ANOVA(Abalysis of variance), Correlation, Correlation statistics
#these methods helps us gain better understanding of the data and understand the relationships between elements 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 


drive_wheels_counts = df['drive-wheels'].value_counts()
drive_wheels_counts.rename(columns = ('drive-wheels':'value-counts'), inplace = True )
df.index.name = 'drive-wheels'

sns.boxplot(x = "drive-wheels", y = "price", data = df)# this pots the boxplot to visualise the categorised values 


#scatter plots are used to show relatuonship between two variables 
#predictor variable on x axis and the target(what to predict) on the y axis .
#here  our predictor c=variable is engine size and the target variable is the price 
#we want to see how the engine size afects the price of a car 

x = df['engine-size']
y = df['price']
plt.scatter(x, y)
plt.title("Scatter plot of engine size against price ")
plt.xlabel("Engine size")
plt.ylabel("Price")
plt.show()

#GROUPBY - GROUPING ELEMENTS 
#here we wull group the data into differenct drive wheels and see their efect on the price independently
#first we pick out all the columns we want 
df_test = df(['drive-wheels', 'body-style', 'price'])

#sp we want to know the average price according to body style and drive wheels 
df_grp = df_test.groupby (['drive-wheels', 'body-style'], as_index = False).mean()

#the data will no be easily visualised by the group function hence we create a pivot table 
df_pivot = df_grp.pivot(index = 'drive-wheels', columns = 'body-style')
#index is the row index while column is the column and the values will be price 

#next we plot a heat map 
plt.pcolor(df_pivot, cmap = "RdBu")
plt.colorbar()
plt.show()

#CORRELATION BETWEEN DIFFERENT VARIABLES 
#Correlation measure the extent to which two variables are related but correlation dosent imply causation. 
#to show the correlation between the engine size and price we use a scatter plot and a regression line 
sns.regplot(x = "engine-size", y = "price", data = df)#scatter plot 
plt.ylim(0, )# Regression line 
plt.show()

#STATISTICAL CORRELATION 
#Pearson correlation is used to measure the strength of correlation between two features 
#It will give you two values: correlation coefficient and p-value 

#CORRELATION COEFFICIENT 
close to +1 = large positive relationship
close to -1 = large negative relationship 
close to 0 = No relationship 


# P-VALUE 
<0.001 = Strong certainity in the result 
<0.05 = Moderate certainity in the result
<0.1 = Weak certainity in the result
>0.1 = No certainity in the result

#Example : we are looking at the correlation between horsepower and car price 
#Here we use SciPy stats package 
Pearson_corr  = stats.pearsonr(df['horsepower'], df['price']) #shows the p value and corr coefficient 
plt.pcolor(Pearson_corr, cmap = "RdBu") #corelation heatmap
plt.ylim(0, )
plt.colorbar()
plt.show ()

#ANALYSIS OF VARIANCE (ANOVA)
#It can be used for finding correlation  between different groups of a categorical variables 
#It gives us the f-test score and the p value (confidence degree)
#small f value implies poor correlation and large f implies stron correlation 
#Example- lets test the analysis of variance between honda and subaru 
#the scipy package is used for this purpose 
anova_test = df(['make', 'price'])
anova_test_group = anova_test.groupby(['make'])
anova_results = stats.f_oneway(anova_test_group.get_group("honda")['price']), anova_test_group.get_group("subaru")['price'])
