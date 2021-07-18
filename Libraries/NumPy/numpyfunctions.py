import numpy as np 

np.arange(start, stop, step, endpoint = True/False)#lists the elements from start to stop and add step if applicable 
np.linspace(start, stop, sample, endpoint = True/False)#retuns numbers spaced evenly based on number given i.e sample 
dtype = datatype #you can specify databy after the list array if needed 
np.shape(rows, columns)
np.mean()
np.median()
np.corrcoef()#check corre;ation betweem two variables 
np.std()#standard deviation 
np.random.normal(mean, std, samples)



#RELATIONAL OPERATORS 
< 
>  
<= 
==
>=
!= #not equal to 


#LOGICAL OPERATORS 
and 
or 
not 


#CONDITIONAL STATEMENTS 
if condition:
    expression
elif condition:#if the first condition is true the elif conditon is neglected by python 
    expression
else:
    expression

#Polynomial regression with one dimension 
f = np.polyfit (x, y, n_degree)#polynomial regression with order n. this transforms the data to polynomial 
np.poly1d(f)# it is used to define a polynomial function. used after transforming the data to polynomials 