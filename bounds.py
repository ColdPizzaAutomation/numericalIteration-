
def fizzBuzz():
    result = (i*multiplier) 
    if result % 2 == 0:
        print ("fizz")
    if result % 2 !=0:
        print ("buzz")


lb = int(input("Please enter your lower-bound integer: "))
ub = int(input("Please enter your upper-bound integer: "))

#stores user input
    
verif = input("\nYou have entered {0} as your lower-bound integer, and {1} as your upper-bound \ninteger. \n\nIf you are content with this sequence, do you wish to proceed? (y/n): ".format(lb,ub))
response = verif.lower()
if lb > ub:
    print ("\nFATAL ERROR: \n\nYour lower-bound input is greater than your upper-bound input. \n\nPlease try again.")

#conditional check to ensure lower bound is strictly less than upper bound
#returns stored input to user, prompts user for response to exe program. User response is made lower-case

if verif =="y":
    for multiplier in range(lb, (ub+1)):
        for i in range(1,20):
            print (i, "x", multiplier, "=", i*multiplier)
            fizzBuzz()
        
if verif != "y":
    print("invalid response, \ntry again.")




