# newly introduced function in phython 3


a= int(input("enter the lucky number between 1 to 10:"))
# match is similar to switch in java
match a:
    case 1:
        print("you won $100")
    case 3:
        print("you won $30")
    case 7:
        print("you won $700")
    #default
    case _: 
        print("better luck next time")