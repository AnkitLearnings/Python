# strings are unmutable
'''
s= "hello world"

print("string in upper case:", s.upper(), "original string:", s)
print("string in lower case:", s.lower())
print("string Capilalize:",s.capitalize())
print("string title:", s.title())


s= " Hello world "
print("string:",s)
print("string strip:",s.strip())        #remove blank space from both ends
print("string strip left:",s.lstrip())  #remove blank space from left end
print("string strip right:",s.rstrip()) #remove blank space from right end


text = "phython is easy and fun and fun"
print(text.find("fun"))                 #return the first index of the first occurance of word
print(text.replace("fun", "crazy"))     #replace all the fun with crazy


car = "Toyota,Kia,Mazda,Honda"
print("car string :", car)
#string to list
print("car string spilt and return list:",car.split(","))   #will return the list of element saperated by ,
#list to string
print(",".join(car.split(",")))                             #will return the string by joining the list element with ,
'''
model = "mazdacx30"
print(model.isalnum())              #True   
print(model.isalpha())              #False
print(model.islower())              #True