# Write a program that counts how many vowels are in a given string.
statement= "I love to travel"
text = statement.lower()
a= text.count("a")
e= text.count("e")
i= text.count("i")
o= text.count("o")
u= text.count("u")
# total = a+e+i+o+u
print("Total wovel in the sentance are:",(a+e+i+o+u) )


vowel = ['a', 'e', 'i', 'o', 'u'] 
sum=0
for char in text:
    if(char in vowel):
        sum+=1
print("Total wovel in the sentance are(using loop):",sum)