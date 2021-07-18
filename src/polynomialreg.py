#Polynomial regression 
#the polyfit function is used to conduct polynomial regression 
import numpy as np 

f = np.polyfit(x, y, 3)#thisn is a third order polynomial regression
#x is the independent v, y is the target v and 3 is the order of regression 
p = np.polyld(f) 
print (p) #the polynomial regression can be printed 

#we can also have multidimension polynomial linear regression 
#numpy cannot handle this so we use the preprocessing library in scikit learn
#this is two dimensional second order polynomial regression 

from skilearn.preprocessing import PolynomialFeatures
pr = PolynomialFeatures (degree = 2)# degree is the order of polynomial regression
pr.fit_transform([1, 2], include_bias = False)

#as the dimension of the data gets larger we may want to normalise some features in scikit learn 
from skilearn.preprocessing import StandardScaler()
Scale = StandardScalar()
Scale .fit(x_data[['horsepower', 'highway-mpg']])#this is used to fit the scale in the model 
#then transform the data into a new dataframe 
x_scale = Scale.transform(x_data[['horsepower', 'hoghway-mpg']])