#also called coefficient of determination 
from skilearn.linear_model import LinearRegression

lm = LinearRegression()

x = df['highway-mpg']
y = df['price']

lm.fit(x, y)
lm.score(x, y)#the score function is used to get the coefficient of determination 
