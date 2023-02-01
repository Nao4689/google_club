def evenOrOdd(testNum):
    x = testNum%2
    if x == 0:
        print("your number is even")
    elif x == 1:
        print("your number is odd")
    
# evenOrOdd(756249)

def tokenChecker(numOftokens,name):
    input_ = numOftokens
    if input_ in [1,2,3,4]:
        print("Sorry", name, ",you need more tickets. :(")
    elif input_ in [5,6,7,8,9]:
        print("Congrats,",name,"! You have won a ring pop. :)")
    elif input_ in [10,11,12,13,14]:
        print("Congrats,", name, "! You have won a kit kat. :)")
    elif input_ in [15,16,17,18,19,20,21,22,23,24]:
        print("Congrats,", name, "! You have won silly putty. :)")
    elif input_ in [25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]:
        print("Congrats,", name, "! You have won a laser pointer . :)")
    elif input_ in [50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]:
        print("Wow, you're good,", name, "! You have won a stuffed animal. :)")
    elif input_ == 100:
        print("Wow, you're good,", name, "! You can pick anything you'd like! :)")

# tokenChecker(56, "naomi") 

import random
    
def diceRoll():
    x = random.randint(1,6)
    print(x)
    y = random.randint(1,6)
    print(y)
    print("I have just rolled 2 dice, the numbers produced are",x, ", and", y)
    ch = input("do you want to add or sub the two numbers? - ")
    if ch == "add":
        print(x+y)
    elif ch == "sub":
        print(x-y)
    else:
        print("I do not understand your response.")

diceRoll() 
    
