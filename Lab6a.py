#----------------------------------------------------------------------
# You are going to have the user fill an array with 10-15 elements that
# include positive, negative, and 0 integer values. You will then analyze
# and report on the data.
#----------------------------------------------------------------------
# Name:          Maria Lomeli
# Date:          November 27, 2021
# Reference:     A6a Lab
# Title:         Categorize Array Elements 
# Inputs:        User enters 10-15 integers (negative, 0, and positive) and
#                -99 to stop entering data.                    
# Process:       Parses through an array of at least 10-15 elements and 
#                determines how many elements are positive, negative, and 0. 
#                Then parses through array to determine sum of all elements. 
# Outputs:       How many elements the arrat had, how many elements are 
#                positive, how many are negative, how many are 0, and 
#                determines sum of all elements.
#-----------------------------------------------------------------------
def main():
    # Initialize Constant
    LOWER_BOUND  = 10

    # Initialize Constant
    UPPER_BOUND  = 15

    # Initialize array 
    numArray     = []

    # Initialize user input
    userInput    = 0

    # Initialize variables
    invalidArray = True          #Count >= 10 and count <= 15
    num          = 0

    # negative values variable
    negativeValuesCount = 0

    # zero value 
    zeroValues          = 0

    # postive values
    postiveValuesCount  = 0 

    # sum of array
    sumArray            = 0
        
  
    
    print("You are going to enter 10-15 integers that must be negative, positive and 0 values.")
    
    # Start while loop to determine if the array has valid number of elements
    while(invalidArray):
        
          # prompt user for input for initial inner while loop iteration    
        userInput = int(input("Please enter value to add to the array (-99 to exit): "))
        while(userInput != -99):
            
            # append the value to the numArray
            numArray.append(userInput)

            # Prompt user for input and if they enter -99 it will end the entry
            userInput = input("Please enter values to add to the array (-99 to exit): ")
            # convert the input to an integer
            userInput = int(userInput)

        # check if the array has enough inputs
        if len(numArray) <= LOWER_BOUND:
            print("# ACTION NEEDED: You were supposed to enter between ", LOWER_BOUND, " and ", UPPER_BOUND, " values. You'll need to enter more.")
        else:
            # If we're here the numArray count is valid and we can exit the validation loop
            invalidArray = False

    # Parse through the user array to determine if postive, negative, zero
    while num < len(numArray) and num < UPPER_BOUND:
        # Check if the current array value is negative
        if int(numArray[num]) < 0:
            negativeValuesCount += int(1)
        # Check if the current array value is 0
        elif int(numArray[num]) == 0:
            zeroValues += int(1)
        # Must be positive
        else:
            postiveValuesCount += int(1)

        # Accumulate the array
        sumArray += int(numArray[num])
        num += int(1)
    
    # Print output     
    print("       Output                  ")
    print("**********************************")
    print("Array    Count         : ", len(numArray))
    print("Positive Values        : ", postiveValuesCount)
    print("Negative Values        : ", negativeValuesCount)
    print("Zero     Values        : ", zeroValues)
    print("Sum      Total         : ", sumArray)

#Call main
main()



