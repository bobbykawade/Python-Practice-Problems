Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = input('bobby:')
bobby:
>>> print(name)

>>> name = input('bobby:')
bobby:
>>> name = input(10+20)
30
>>> name = input(10+20:)
SyntaxError: invalid syntax
>>> name = input('enter your name:')
enter your name:bobby
>>> print(name)
bobby
>>> a = input('enter the first integer:')
enter the first integer:10
>>> b = input('enter the second integer:')
enter the second integer:20
>>> print(a+b)
1020
>>> a = int(input('enter the first integer:'))
enter the first integer:10
>>> b = int(input('enter the second integer:'))
enter the second integer:20
>>> print(a+b)
30

>>> li = [1,2,3,4,5]
>>> print(type(li))
<class 'list'>
>>> a = [1,3,5,7,9]
>>> b = ['abc', 'xyz', 'pqr']
>>> x = [1,2,'abc',50]
>>> s = [1,1,2,[22,33,44,55],'aaaa',[1,2,['abc',[300,500]],800]]
>>> print(s)
[1, 1, 2, [22, 33, 44, 55], 'aaaa', [1, 2, ['abc', [300, 500]], 800]]
>>> print(len(s))
6
>>> print(len(a
>>> print(s[500])
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(s[500])

>>> print(s[5])
[1, 2, ['abc', [300, 500]], 800]
>>> print(s[-1][0])
1
>>> print(s[-2][1])
a
>>> print(s[-4][2])
    print(s[-4][2])
TypeError: 'int' object is not subscriptable
>>> print(str(s[-1][2][1][1]))
500
>>> print(str(s[-1][2][1][1][:2]))
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(str(s[-1][2][1][1][:2]))
TypeError: 'int' object is not subscriptable
>>> print(str(s[-1][2][1][1][:2])
	  50
	  
SyntaxError: invalid syntax
>>> li = [1,2,3,4]
	  
>>> li.append('python')
	  
>>> print(li)
	  
[1, 2, 3, 4, 'python']
>>> [1, 2, 3, 4, 'python']
	  
[1, 2, 3, 4, 'python']
>>> 
	  
>>> li = [1,2,3,4]
	  
>>> li.append('python')
	  
>>> li.insert(2,'abc')
	  
>>> print(li)
	  
[1, 2, 'abc', 3, 4, 'python']
>>> del li[4]
	  
>>> print(li)
	  
[1, 2, 'abc', 3, 'python']
>>> li[1] = 100
	  
>>> print(li)
	  
[1, 100, 'abc', 3, 'python']
>>> li[2] = 200
	  
>>> print(li)
	  
[1, 100, 200, 3, 'python']
>>> del li[1:4]
	  
>>> print(li)
	  
[1, 'python']
>>> [1, 'python']
	  
[1, 'python']
>>> 
	  
>>> ti = (1,2,3,4,5,6)
	  
>>> print(ti[0])
	  
1
>>> li = [1]
	  
>>> ti = (1)
	  
>>> print(type(li),type(ti))
	  
<class 'list'> <class 'int'>
>>> <class 'list'> <class 'int'>
	  
SyntaxError: invalid syntax
>>> li = [1]
	  
>>> ti = (1,)
	  
>>> print(type(li),type(ti))
	  
<class 'list'> <class 'tuple'>
>>> <class 'list'> <class 'tuple'>
	  
SyntaxError: invalid syntax
>>> 
	  
>>> a = 'python'
	  
>>> a[0] = 'v'
	  
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a[0] = 'v'
TypeError: 'str' object does not support item assignment
>>> a = 'python'
	  
>>> b = 'v' + a[1:]
	  
>>> print(a+b)
	  
pythonvython
>>> di = {1:'one',2:'two'}
	  
>>> print(di)
	  
{1: 'one', 2: 'two'}
>>> di['one'] = 100
	  
>>> di[1] = 500
	  
>>> print(di)
	  
{1: 500, 2: 'two', 'one': 100}
>>> del di[2]
	  
>>> print(di)
	  
{1: 500, 'one': 100}
>>> del di[0]
	  
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    del di[0]
KeyError: 0
>>> print(di)
	  
{1: 500, 'one': 100}
>>> print(di['one'])
	  
100
>>> marks = {1:{'subj1':90,'subj2':78,2:{},3:{},4:[78,98,96,67]}
	     marks[3]['subj2']
	     
SyntaxError: invalid syntax
>>> month_no = 3
             months = {1:'jan',2:'feb',3:'mar'}
             months_list = ['jan','feb','mar']
             print(months_list[month_no-1])
             
                       
