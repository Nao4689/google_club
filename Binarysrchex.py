#linear ex
def linearS(ln,tn):
    for i in ln:
        print(i)
        if i == tn:
            break
    print("the target is:", i)
    
# linearS(range(101), 56)
    
#binary ex
def binaryS(ln,tn):
    low = ln[0]
    high = ln[-1] 
    compguess = int((low+high)/2)
    while compguess != tn:
        if compguess < tn:
            low = compguess
        else: 
            high = compguess
        print(compguess)
        compguess = int((low+high)/2)
        
    print("the target num is ", compguess)
                
        
# binaryS(range(101), 6)

def guessMyNumber(): 
    print("Think of a number between 0 - 100")
    x = range(101)
    min = 0
    max = 100
    guess = 0
    while guess != "c":
        guess = int(min + max/2)
        y = input("is your number" + str(guess) + "?(put h if its too high or l if it is too low, and c for if the answer is correct) ")
        if y == "l":
            min = guess
        elif y == "h":
            max = guess
        elif y == "c":
            print("your number is", guess)
            break
    

guessMyNumber()       
