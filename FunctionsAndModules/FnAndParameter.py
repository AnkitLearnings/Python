#Positional Arguments
def add(a,b):
    return a+b
print("Positional Arguments \nAddtion of 2 numbers:",add(3,6))

#Default Arguments
def multiplication(a,b,c=3):
    return a*b*c
print("Default Arguments \nmultiple :", multiplication(1,2))

#Keyword Arguments
print("Keyword Arguments \naddition", add(b="world", a="hello "))