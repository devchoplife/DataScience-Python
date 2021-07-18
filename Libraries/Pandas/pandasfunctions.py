import pandas as pd 
dataframe = df 

pd.read_csv ("file_path", index_col = 0) #to import csv files 
index_col = n #this can be added to the read_csv function to note the index column 
df.column #to se;ect a column (called dot notation)
df["column"] #to also select a column 
df["row_index"] # to select a row 
df.loc["row_label", "column"] or df["column"].loc["row_label"]#to display specific row and label 
df.dtypes()#used to check the datatypes of the dataframe 
df.describe()#statistical summary of the data. it skips blanks by default 
df.describe(include = "all") # shows statistical summary of all the data including blanks
df.info()#shows the first 30 rows and last 30 rows 
df.dropna(subset = [column], axis = 0/1, inplace = True)#subset specifies the column to look for null values
#inplace makes sure the table is modified 
df,dropna(axis = 0) #drops the entire row that contains missing values 
df.dropna(axis = 1) #drops the entire row that contains missing values 
df.replace([missing_value], [new_value])#note that nan is a numpy error and is rep by np.nan 
df.rename(columns = [column = (old_name:new_name), inplace = True)
df.astype()#to convert a column into another data type . Check the type first before converting 
.isin()#used t select values
.unique () #to see a list of unique values 

#Data normalization makes the range consistent so advanced statistical analysis will be accutrate e.g linear regression. For example age and income ranges are far apart and might need to be normalised. so we convert them to a range between zero and one to get perfect analysis . There are three type of data normalisation

#1 SIMPLE FEATURE SCALING 
x_new = x_old / x_max

#MIN-MAX
x_new = x_old - x_min / x_max - x_min

#Z-SCORE OR STANDARD SCORE 
x_new = x_old - x_avg / x_std

pd.cut(test_column, bins, labels, include_lowest = True/False)#to finally bin the data . you can first define the bins, group names and the test column as object before using the cut function to bin them 
pd.get_dummies(df[column_name])# to convert categorical variables into quantitative variables 
df.value_counts() # counts the numbers of categories in a categorical data e.g. count distinct products in a product category 
df.index.name()#specify row index name for a new table 
df.groupby(category1, category2, as_index = True/False)#it groups categorical variables but make sure you call out all the data you need first 
df.pivot (index = , column = )#creates a pivot table 

