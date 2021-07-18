x = ["a","b","c"]
y = x #This means that y is referencing x so any change you make to y will also affect x
#To fix this we write y this way
y = list(x)#here any change made to y will not affect x anymre 