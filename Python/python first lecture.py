Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('hello world')
hello world
>>> print(100)
100
>>> print('20')
20
>>> print(10+2)
12
>>> print(11%2)
1
>>> print(10*2)
20
>>> print(10/2)
5.0
>>> print(10-2)
8
>>> X='abc'
>>> num=100
>>> print(x)
Traceback (most recent call last:
  File "<pyshell#10>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
>>> a = 10
>>> b = 20
>>> c = a+b
>>> print('c')
c
>>> print('a+b')
a+b
>>> a = "python"
>>> print(a[0])
p
>>> print(a[50])
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(a[50])
IndexError: string index out of range
>>> 
>>> a = "python"
>>> a = 100
>>> print(a)
100
>>> a = "python"
>>> print(a[1:4])
yth
>>> full_name = 'bobby kawade"
SyntaxError: EOL while scanning string literal
>>> full name = 'bobby kawade'
SyntaxError: invalid syntax
>>> full_name = 'bobby kawade'
>>> first_name =
SyntaxError: invalid syntax
>>> full_name = 'bobby kawade'
>>> first_name = 'bobby'
>>> last_name  = 'kawade'
>>> print(first_name, last_name)
bobby kawade
>>> full_name = 'abc xyz'
>>> first_name = full_name[0:3]
>>> last_name = full_name[4:7]
>>> print(first_name)
abc
>>> print(last_name)
xyz
>>> print(full_name[:])
abc xyz
>>> print(full_name[::3])
a z
>>> print(full_name[::-1])
zyx cba
>>> print(full_name[-1])
z
>>> print(full_name[0])
a
>>> s = 'programming'
>>> s = 'programming'
>>> first_name = 'bobby'
>>> last_name = 'kawade'
>>> print('my full name is "first_name+last_name)
	  
SyntaxError: EOL while scanning string literal
>>> first_name = 'bobby'
	  
>>> last_name = 'kawade'
	  
>>> print('My full name is"' + first_name + '' + last_name + '"')
	  
My full name is"bobbykawade"
>>> a = "abc'xy\"z"
	  
>>> print(a)
	  
abc'xy"z
>>> a = 'abc"xy\'z'
	  
>>> print(a)
	  
abc"xy'z
>>> a = abc
	  
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a = abc
NameError: name 'abc' is not defined
>>> a = 'abc'
	  
>>> b = 10
	  
>>> print(a+b)
	  
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print(a+b)
TypeError: can only concatenate str (not "int") to str
>>> a = 'abc'
	  
>>> b = 10
	  
>>> b = str(b)
	  
>>> print(a+b)
	  
abc10
>>> a = 'abc'
	  
>>> b = 10
	  
>>> c = str(b)
	  
>>> print(a+c)
	  
abc10
>>> x= '100'
	  
>>> y = 200
	  
>>> print(int(x)+y)
	  
300
>>> 
