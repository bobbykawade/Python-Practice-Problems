# # -*- coding: utf-8 -*-
# """
# Created on Sun Mar 10 20:36:39 2019

# @author: DELL
# """

#  #    
# #li = [1,2,3,4,5,6,7,8,9,10]
# for x in li:
#        print(x)
# for x in 'abcde':
#     print(x)

#     #
#     for e in li:
#         if e%2 ==1:
#             print(e)
# print(len(li))


# #li = [1,2,3,4,5,6,7,8,9,10]
# count = 0
# for i in li:
#      count = count + 1
#      print(count)
    
# li = ['a',1,2,'b']
# count = 0
# for i in li:
#     count = count + 1
#     print(count)
# for x in li:
#     sum=sum
#     print(sum)

    
#     sum = 0
#     for x in li:
#     sum=sum + x
#     print(sum)
    
    
    
    
# #for
# li = ['a',1,2,'b']
# count = 0
# for i in li:
#     count = count + 1
#     print(count)
    
# #for loop
# li = ['abc','Ubuntu','ppp','Udacity']
# count = 0
# for e in li:
#     if e[0] == 'U':
#         count = count + 1
#         print(e)
    
# #while loop 

# a = 0
# while a < 11:
#     print(a)
#     a += 1
    
#     #substring
#     a = 'Hello World'
#     print(a[2:5])
    
#     #string
#     a = 'Hello World'
#     print(a[1])
    
#     #Strip Method
#     a = ' Hello, World! '
#     print(a.strip())
    
#     #len method
#     a = 'Hello, World!'
#     print(len(a))
    
#     #lower method
#     a = 'HELLO, WORLD!'
#     print(a.lower())
    
#     #upper method
#     a = 'hello, world!'
#     print(a.upper())
    
#     #replace method
#     a = 'Hello World'
#     print(a.replace('H', 'J'))
    
#     #split method
a = 'Hello World'
print(a.split(' '))
    
#     #lists []
# x = ['apple', 'banana', 'strawberry']
# print(x)
    
#    #access items
# x = ['apple', 'banana', 'strawberry']
# print(x[1])
    
#     #change item value
#     x = ['apple', 'banana', 'strawberry']
#     x[1] = 'blackcurrent'
#     print(x)
    
#     #for loop
#     #li = ['apple', 'banana', 'cherry']
#     for x in li:
#         print(x)
        
#     #li = [1,2,3,4,5,6,7,8,9,10]
#     sum = 0
#     for x in li:
#             sum=sum + x
#             print(sum)
        
#     #if loop
#     thislist = ["apple", "banana", "cherry"]
#     if "apple" in thislist:
#         print("Yes, "apple" is in thislist")
        
#         #while loop
    
#     #x = [1,2,3,4,5]
#     total = 0
#     index = 0
#     while index < len(x):
#         total += x[index]
#         index += 1
#         print(total)
        
#     # List length
#     li = ['a', 'b', 'c']
#     print(len(li))
            
#     #append method()- add item to the end of this list
#     li = ['a', 'b', 'c']
#     li.append('x')
#     print(li)
  
#     #insert method()
#     li = ['a', 'b','c']
#     li.insert(1, 'x')
#     print(li)
    
#     #remove item()
#     li = ['a', 'b', 'c']
#     li.remove('b')
#     print(li)
    
#     #pop method(remove method type)
#     li = ['a', 'b', 'c']
#     li.pop(2)
#     print(li)
    
#     #del keyword
#     li = ['a', 'b', 'c']
#     del li[0]
#     print(li)
    
#     li = ['a', 'b', 'c']
#     del li
#     print(li)
    
#     #clear method()
#     li = ['a', 'b', 'c']
#     li.clear()
#     print(li)
    
#     #list constructor
#     li = list(('a', 'b', 'c'))
#     print(li)
    
#     #integer
#     #x = 2504
#     x = str(x)
#     y = int(x[-1] + x[1:-1] + x[0])
#     print(y)
    
#     #loop
    
#     li = [1,2,3,4,5,6,7,8,9,10]
#     for x in li:
#         sum=sum
#         print(sum)
        
#     #second lecture
#      month_no = 3
#      months = {1:'jan',2:'feb',3:'mar'}
#      months_list = ['jan','feb','mar']
#      print(months_list[month_no-1])
        
    
   
#     #tuples- collection which is ordered and unchangeble
#     thistuple = ()
#     #count tuple() returns the no. of times a specified value occurs in tuple
    
#     #index tuple() searches the tuple for a specified value and returns the 
#      position of where it was found
            
     
#      #sets {} collection which is unordered and unindexed.
#      no access items
#      use loop through set items
#      #in loop for sets
#      li = ['apple','banana','cherry']
#      print('banana' in li)
     
#      #dictionaries {} collections which is unordered, changeble & indexed
     
#      li = {'brand':'ford','model':'mustang','year':1964}
#      print(li)
#      li['year'] = 2018
#      x = li['model']
#      x = li.get('model')
     
#     #for loop dictionary    
#     li = {'brand':'ford','model':'mustang','year':1964}
#      for x in li:
#          print(li[x])
         
#          li = {'brand':'ford','model':'mustang','year':1964}
#          for x in li:
#              print(x)
             
#              li = {'brand':'ford','model':'mustang','year':1964}
#              for x  in li.values():
#                  print(x)
                 
#                  li = {'brand':'ford','model':'mustang','year':1964}
#                  for x, y in li.items():
#                      print(x, y)
                     
#             li = {'brand':'ford','model':'mustang','year':1964}
#             if 'model' in li:
#                 print('Yes, 'model' is one of the key in the li dictionary')
                
#      #add items in dictionary
#      li = {'brand':'ford','model':'mustang','year':1964}
#      li['color'] = 'red'
#      print(li)
     
     
#      #conditional statements-
     
#      #if statement
#      a = 33
#      b = 200
#      if b>a:
#          print('b is greater than a')
     
#     #indentation error is whitespace
#     a = 33
#     b = 200
#     if b>a:
#     print ('b is greater than a')
    
#     #elif condition if previous condition were not true then try this condition
#     a = 33
#     b = 33
#     if b>a:
#         print('b is greater than a')
#     elif a==b:
#         print('b is equal to a')
        
#     #else condition for more than two conditions
#         a = 200
#         b = 33
#         if b>a:
#             print('b is greater than a')
#         elif a==b:
#             print('b is equal to a')
#         else:
#             print('a is greater than b')
            
#             #short hand of if
#             a = 200
#             b = 33
#             if a>b:print('a is greater than b')
            
#             #short hand of if...else
#             a = 200
#             b = 33
#             print('A') if a>b else print('B')
            
#             #multiple else statement with three conditions
#             a = 200
#             b = 33
#             print('A') if a>b else print('=') if a==b else print('B')
            
#             #and keyword logical keyword use to combine conditional statement
#             a, b, c = 2, 1, 3
#             if a > b and c > a:
#                 print('Both conditions are true')
                
#             #or keyword
#                 a, b, c = 2, 1, 3
#                 if a > b or a > c:
#                     print('At least one of the condition is True')
                    
#                     #primitive loop command
                    
#             #while loop we can execute a set of statement as long as 
#                     a condition is true.
                    
#                     i = 1
#                     while i < 6:
#                         print(i)
#                         i += 1
                        
#             #break statement
#             i = 1
#             while i < 6:
#                 print(i)
#                 if i == 3:
#                     break
#                 i += 1
                
#            #continue statement
           
#            i = 0
#            while i < 6:
#                i += 1
#                if i == 3:
#                    continue
#                print(i)
               
#           # for loop used to iterate over a sequence
          
#           li = ['apple','banana','cherry']
#           for x in li:
#               print(x)
              
#               #break statement in for loop
              
#           li = ['apple','banana','cherry']
#           for x in li:
#               print(x)
#               if x == 'banana':
#                   break
              
#                 *not run
#                 li = ['apple','banana','cherry']
#                 for x in li:
#                     if x == 'banana':
#                     break
#                 print(x)
                
#          #range function() to loop through a set of code for specific no. of 
#          times
         
#          for x in range(7):
#              print(x)
             
#              for x in range(2, 6):
#                  print(x)
                 
#                  for x in range(2, 30, 3):
#                      print(x)
                     
                     
#         #else in for loop
#         else keyword in for loop specifies a block of code to be executued
#         when the loop is finished.
        
#         for x in range(6):
#             print(x)
#         else:
#             print('finally finished')
            
            
#             # nested loop[] a loop inside a loop or inner loop
            
#             adj = ['red','big','tasty']
#             fruits = ['aaple','banana','cherry']
#             for x in adj:
#                 for y in fruits:
#                     print(x,y)
                    
#                     #problem
                    
                        
#         li = [11,340,8,8709,45] => 1+1+3+4+0+8+7+0+9+4+5
#         multiplication table
#         1 * 1 = 1
#         1 * 2 = 2
#         .
#         .
#         1 * 10 = 10

#         #''' Functions
#         - function defination
#         - function calling
#         '''
#         def display(s):
#             return s
#             output = display('abc')
#             print(output)
            
#             def add_two_nos(num1,num2):
#                 return num1 + num2
#                 print(num1+num2)
#                 return 'Done'
                
                
#                 output = add_two_nos(2,4)
#                 print(output)
        
#         a = 2
#         b = 4
#         output = add_two_nos(a,b)
#         print(output)
            
#         # empty lists [] A = []
#         # empty dictionaries {} A = {}
        
#         li = []
#         for _ in range(7):
#             elem = input('enter an element')
#         li.append(elem)
        
        
#         li = [a,b,c]
#             ans = max_of_three(2,1,3)
            
            
#         '''
#         def max_of_three(a,b,c):
#             if a>b and a>c:
#                 return a
#             elif b>a and b>c:
#                 return b
#             else:
#                 return c
#                 print(max_of_three(44,200,54))
#                 '''
                
#                 #
#                 '''
#                 def test(a):
#                     return 'done1'
#                     print('done2')
#                     print(a)
                   
                    
                    
                    
#                     def test2(a):
#                         return a
#                     ans2 = test2('abc')
#                     print(ans2)
                    
#                     '''
#                     def test(a):
#                         print('a')
#                         ans = test('abc')
#                         print(ans)
#                     '''
                    
                    
#                     #problems
#                    - max elelments on list of integer[22,33,1,234,56,21] =>234
#                    -['abcd','aa','python','axdd'] => 'python
#                     -longest word
#                     'aabbaccab' => {'a':4,'b':3,'c':2}
                    
                    
#                     #
#                     #li = [22,33,1,234,56,21]
#                     def max_of_list(li):
#                         max_value = li[0]
#                         for elem in li[1:]:
#                             if elem > max_value:
#                                 max_value = elem
#                         return max_value
#                     print(max_of_list([22,33,1,234,56,21]))
                    
                    
#                     # li = ['abcd','aa','python','axdd']
#                     def find_longest_word(li):
#                         longest_word = li[0]
#                         for word in li:
#                             if len(word) > len(longest_word):
#                                 longest_word = word
#                         return longest_word
#                     print(find_longest_word(['abcd','aa','python','axdd']))
                    
                    
#                     #'aabbaccab' => {'a':4,'b':3,'c':2} dictionary
#                     #li = {'aabbaccab'}
#                     def dictionary(li):
#                         x = {}
#                         for char in li:
#                             if char in x:
#                                 x[char] += 1
#                             else:
#                                 x[char] = 1
#                         return x
#                 print(dictionary('aabbaccab'))
                        
                        
#                 #pythontutor.com        
                
#                 #indian currency
#                 #li = '12734'
#                 def currency_format(li):
#                     if len(li)<=3:
#                         return li
#                     else:
#                         li=li[::-1]
#                         t=li[:3]
#                         t=t+','
#                         c=0
#                         for i in range(3,len(li)):
#                             t=t+li[i]
#                             c=c+1
#                             if c==2:
#                                 t=t+','
#                                 c=0
#                                 if len(li)%2!=0:
#                                     t=t[:-1]
#                                     return t[::-1]
#                 print(currency_format(li))
                    
                    
                    
#                     #pangram 
#                     #guess the number
                    
                    
#                     ## ---(Sun Mar 24 16:04:52 2019)---
# class Student:
#     university = 'Mumbai University' #class attribute
#     student_1 = Student()
#     print(Student.university)


# class Student:
#     university = 'Mumbai University' #class attribute
#     student_1 = Student()
#     print(Student.university)


# print(Student.university)
# class Student:
#     university = 'Mumbai University' #class attribute
#     student_1 = Student()
#     print(Student.university)


# class Student:
#     university = 'Mumbai University' #class attribute
#     student_1 = Student()
#     print(student.university)


# class Student:
#     university = 'Mumbai University'
#     def_init_(self):
#         print('an object is created')


# class Student:
#     university = 'Mumbai University'
#     def__init__(self):
#         print('an object is created'


# class Student:
#     university = 'Mumbai University'
#     def __init__(self):
#         print('an object is created')


# class Student:
#     university = 'Mumbai University'
#     def __init__(self):
#         print('an object is created')
#         student_1 = Student()


# class Student:
#     university = 'Mumbai University'
#     def __init__(self):

# print('an object is created')
# class Student:
#     university = 'Mumbai University'
#     def__init__(self):
#         self.status = 'Active'
#         student_1 = Student()
#         print(student_1.status)


# class Student:
#     university = 'Mumbai University'
#     def__init__(self):
#         self.status = 'Active'
#         student_1 = Student()
#         print(student_1.status)


# class Student:
#     university = 'Mumbai University'
#     def__init__(self):
#         self.staus = 'Active'
#         def change_status(self, new_status):
#             self.status = new_status
#             student_1 = Student()
#             student_2 = Student()
#             student_1.change_status('Suspended')
#             student_2.change_status('Terminated')
#             print(student_1.status)
#             print(student_2.status)


# class Student:
#     university = 'Mumbai University'
#     def __init__(self):
#         self.staus = 'Active'
#         def change_status(self, new_status):
#             self.status = new_status
#             student_1 = Student()
#             student_2 = Student()
#             student_1.change_status('Suspended')
#             student_2.change_status('Terminated')
#             print(student_1.status)
#             print(student_2.status)


# print(student_1.status)
# print(student_2.status)
# class Student:
#     university = 'Mumbai University'
#     def__init__(self):
#         self.status = 'Active'
#         student_1 = Student()
#         print(student_1.status)
        
        
#         class Student:
#             university = 'Mumbai University'
#             def __init__(self):
#                 self.staus = 'Active'
#             def change_status(self, new_status):
#                 self.status = new_status
#         student_1 = Student()
#         student_2 = Student()
#         student_1.change_status('Suspended')
#         student_2.change_status('Terminated')
#         print(student_1.status)
#         print(student_2.status)


# print(student_1.status)
# print(student_2.status)

# class Student:
#     university = 'Mumbai University'
#     def __init__(self):
#         self.staus = 'Active'
#     def change_status(self, new_status):
#         self.status = new_status

# student_1 = Student()
# student_2 = Student()
# student_1.change_status('Suspended')
# student_2.change_status('Terminated')
# print(student_1.status)
# print(student_2.status)
                    
                    
                    
                    
                    
