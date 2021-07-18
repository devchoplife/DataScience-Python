z = 6

if z % 2 == 0:
	print ("z is divisible by 2")
elif z % 3 == 0:
	print ("z is divisible by 3")#this adds another condition to the if condition
else:
	print ("z is neither divisible by 2 nor by 3")
	#the outpit here will be the first expression because once python bumps into a true statement it stops there
	#and will no bother to execute the elif function
	