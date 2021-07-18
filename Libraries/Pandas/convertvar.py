#WE FOCUS ON TURNING CATEGORICAL VARIABLES INTO QUANTITATIVE VARIABLES 
#because most statistical models cannot take strings/objects  as inputs
#a way of doing it is  ONE-HOT ENCODING 
#For example 
import pandas as pd 
pd.get_dummies(df["fuel"]) #for example if a list of cars uses diesel and gas as fuel and we apply this. another set of columns are created for each distinct fuel type and either 0 or 1 would be assigned to each car. 1 for the fuel ty[e the car uses and 0 for the rest  
