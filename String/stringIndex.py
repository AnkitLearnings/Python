
name= "Ankit"       # using double quote
place = 'New Zealand'        #using single quote
address = '''Christchurch   
south island
8001'''             #multipleline string, can use ''' ''' or """ """

print(name)
print(place)
print(address)

#  string index start with 0 and negative index start with -1

print("0 index of name:",name[0])
print("-1 index of name:", name[-1])

#   string slicing

#WAP to print first 3 character of the name
print(name[0:3])    #Ank

#WAP to print skip 1 charter 
print(place[0:9:2])     # place[0:9:n] skip n-1 character   #NwZaa
print(address[:7])      #similar to address[0:7]            #Christc
print(place[2:])         #similar to addres[2:length-1]     #w Zealand

print(place.count("a"));    #will count howmany a are available

print(place[::-1])          #reverse the string o/p dnalaeZ weN
print(place[::2])           #skip every alternative charater o/p NwZaad

