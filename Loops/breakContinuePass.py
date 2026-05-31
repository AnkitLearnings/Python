# break
print("WAP to print 1 to 10 but stop loop while reached to 6")
for i in range(1,11):
    if(i==6):
        break
    print(i)

# continue
print("WAP to print 1 to 10 and skip number 6 to print")
for i in range(1,11):
    if(i==6):
        continue
    print(i)


#   pass : when you dont want to do nothing. you are creating the code but implement later 

i= 3

if(i==3):
    pass

print("This is the example of the pass statement")