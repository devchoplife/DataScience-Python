import pandas as pd 

brics = pd.read_csv ("path_to_the_csv_file", index_col = 0)#this command imports the csv file. brics is data name 
#the index column is used to tell python that the first column contains the row indexes 
#then the file gets imported properly 

brics["country"]# this will access the country column
brics.country #this also accesses the country column

brics ["on_earth"] = [true, true, true, true, true]# this adds a new column on_earth to the table with values true
#you can calculate based on other columns to generate new columns 

brics ["density"] = brics ["population"] / brics ["area" * 1000000`]
#it is multiplied by 1 million because the population is represented in millions

brics.loc ["BR"]# this is used to access the row with row index BR 
#you can also specify a row and colum in thec.loc function
brics.loc ["BR", "Country"]#this is the first method 
brics ["Country"].loc ["BR"]#this is the second method of accessing rows
brics.loc ["BR"] ["country"]#this is the third method 