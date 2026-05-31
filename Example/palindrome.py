# Take a user input string and check if it is a palindrome (same forwards and backwards).

text = input("enter a text:")

reverseText = text[::-1]

if(text == reverseText):
    print("Text is a palindrome")
else:
    print("Text is not a palindrome")