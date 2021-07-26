#global variable and local variable

#handling exception in python
#store exact error message
try:
	a = 10
	b = 'abc'
	print(a/b)
except:
	print('enter valid nos.')


	#
	try:
	a = 10
	b = 'abc'
	print(a/b)
except Exception as e:
	print('an error occured:,'e)
finally:
	print('test')