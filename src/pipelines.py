from skilearn.preprocessing import PolynomialFeatures
from skilearn.linear_model import LinearRegression
from sillearn.preprocessing import StandardScalar
from skilearn.pipeline import Pipeline 
#we import all the libraries to get a prediction 

#then we create a list of tuples
Input = [('scale', StandardScaler()), ('polynomial', PolynomialFeatures(degree = 2)), 'mode', LinearRegression()]
#the first elements contain the estimators while the ssecond elements contain the model constructors

#then we input the list into the pipeline constructor 
pipe = Pipeline(Input)

#we can also train the pipeline 
pipe.fit (df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y)
#then we produce a prediction
yhat = Pipe.predict(x[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])

#this method normalises, produces a polynomial transform then outpiuts the prediction 