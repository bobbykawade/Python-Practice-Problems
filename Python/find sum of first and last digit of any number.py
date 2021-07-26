#find sum of first and last digit of any number
# x = '123456789'
# #z = len(x)
# z1 = int(x[0]), int(x[-1])
# print(z1)

#swap first and last digits of any number
# x = '1234567891234376546364'
# #print(len(x))
# z = x[-1]
# z1 = x[0]
# z2 = x[1:-1]
# print(z+z2+z1)

# #swap first and last digit of the list
# def swaplist(newlist):
# 	newlist[0], newlist[-1] = newlist[-1], newlist[0]
# 	return newlist
# newlist = [12,34,56,76,23]
# print(swaplist(newlist))

#print nos from 225-750

# a = 224
# while a < 750:
# 	a += 1
# 	print(a)

# for x in range(225,751):
# 	print (x)

# print(*range(225,750))

#divisible by three or seven

# for x in range(1,100):
# 	if x % 3 == 0 or x % 7 == 0:
# 		print(x)

# n=0
# while n<100:
#     if n%3==0 or n%5==0:
#     	print(n)
#     n += 1
    
#sum of first 100 integers
# x = sum(range(0,101))
# print(x)

# print(sum(range(0,101)))

#sum of all odd numbers from 1 to n
# s = 0
# for x in range(1,100):
# 	if (x+1)%2 == 0:
# 		s = s + x
# print(s)

#multi of first 100 integer
# d = 1
# for x in range(1,100):
# 	d = d*x
# print(d)

# #multiplication table
# d = 12
# for x in range(1,11):
# 	print(d,"multiply by",x,"=",d*x)

#sum of all elements in the lists
# x = [1,2,3,4,5,6,7,8,9]
# print(sum(x))

#sum of all individual digits from a list of integer
# li = [57,67,98]
# a = str(li)
# x = [int(a[1]), int(a[5]), int(a[9])]
# y = [int(a[2]), int(a[6]), int(a[10])]
# b = sum(x[0:3])
# c = sum(y[0:3])
# print(b,c)
# z = [sub.split() for abc in a for sub in abc]
# print(z)

li = [573,678,7564]
a = str(li)
for x in a:
	y = len(x)
	#y = x.split(' ')
	print(y)

#Write a program which takes a number as input from user (n) and prints the sum of only multiples of three or five from 1-n, e.g. 3+5+6+9+10+12+15 for n=17
