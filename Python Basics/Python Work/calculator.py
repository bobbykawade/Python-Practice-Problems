#Basic Calculator

def compute(n1, operator, n2):
	if operator == "+":
		print(n1 + n2)
	elif operator == "-":
		print(n1 - n2)
	elif operator == "*":
		print(n1 * n2)
	elif operator == "/":
		print(n1 / n2)
	else:
		print("Operators or values not recognised.")
N1 = int(input("Enter first value:"))
Operator = int(input("Enter operator:"))
N2 = int(input("Enter second value:"))
a = compute(N1, Operator, N2)
print(a)