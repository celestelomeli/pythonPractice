# You are going to analyze 3 integers entered by the user.
#----------------------------------------------------------------------
# Name:          Maria Lomeli
# Date:          October 30, 2021
# Reference:     A2b Lab
# Title:         Analyze 3 integers
# Inputs:        User enters 3 integers one at a time                    
# Process:       Determines if 3 integers are divisible by 2 and 3
# Outputs:       Shows if integer is divisible by 2 and 3
#-----------------------------------------------------------------------
def main():
    # Declare & Initialize variables
    # Declare & Initialize user Number
    userNumber       = 0
    # Declare & Initialize if integer is divisible by two
    divByTwoResult   = 0
    # Declare & Initialize if integer is divisible by three
    divByThreeResult = 0
    
    # Declare & Initialize for loop count
     
    for count in range(3):
        # call getInt function
        userNumber       = getInt()
        # call divByTwo function and pass user input
        divByTwoResult   = divByTwo(userNumber)
        # call divByTwo function and pass user input
        divByThreeResult = divByThree(userNumber)
        # show results for user input and function return values
        showResults(userNumber, divByTwoResult, divByThreeResult)

        # Re initialize values
        userNumber       = 0
        divByTwoResult   = 0
        divByThreeResult = 0
        print("\n")

# Function definitions 

# getInt() gets integer value from user and returns integer
# -------------------------------------------------------
def getInt():
    userNumber = input("Please enter an integer value: ")
    return int(userNumber)

# divByTwo(userNumber) recieves a number and returns True if divisible by 2 and false otherwise
# -------------------------------------------------------------------------------------
def divByTwo(userNumber):
    if((userNumber % 2) == 0):
      return True
    else:
      return False

# divByThree(userNumber) recieves number and returns True if divisible by 3 and false otherwise
# ---------------------------------------------------------------------------------------
def divByThree(userNumber):
    if((userNumber % 3) == 0):
       return True
    else:
       return False

# showResults receives an integer and two booleans and prints results of if number is divisible by 2 and 3
# -------------------------------------------------------------------------------------------
def showResults(userNumber, divByTwoResult, divByThreeResult):
   if(divByTwoResult == True):
      print("Your number ", userNumber, " is divisible by two")
   else:
      print("Your number ", userNumber, " is not divisible by two")

   if(divByThreeResult == True):
      print("Your number ", userNumber, " is divisible by three")
   else:
      print("Your number ", userNumber, " is not divisible by three")

# call main function
main()
