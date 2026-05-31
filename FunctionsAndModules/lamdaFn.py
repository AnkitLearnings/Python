#function version
def add(a,b):
    return a+b
print("Without lamda \nAddtion of 2 numbers:",add(3,6))
#lamda version
sum = lambda a,b: a+b
print("With lamda \nAddtion of 2 numbers:",sum(3,6))
