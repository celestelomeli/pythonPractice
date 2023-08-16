#----------------------------------------------------------------------
# You are going to design a progam that uses the following parallel arrays:
# employeeID, hoursWorked, payRate, grossPay, stateTaxWHeld. The program
# should relate the data in each array through the subscripts. 
#----------------------------------------------------------------------
# Name:          Maria Lomeli
# Date:          November 27, 2021
# Reference:     A6b Lab
# Title:         Parallel arrays
# Inputs:        8 employees' hours for the past week
#                8 employees' pay rates
# Process:       Gross wages for each employee calculated as well as federal
#                state taxes to be witheld based on the gross wages. 
# Outputs:       For all 8 employees:
#                employee ID, gross pay, federal tax witheld, state tax withheld
#---------------------------------------------------------------------

def main():

    # Initialize Constants
    ARRAY_SIZE = 8
    FED_TAX = 0.15
    STATE_TAX = 0.10

    # Initialize employee ID variable
    employeeID = ["ADS445", "GXS765", "XCZ039", "QPC411", "JSU777", "WHO123", "YOU456", "POP999"]

    # Initilize hours worked array
    hoursWorkedArray = []

    # Initialize pay rate array
    payRateArray = []

    # Initialize  gross pay array
    grossPayArray     = []

    # Initialize federal tax withheld
    fedTaxWheld       = []

    # Initialize state tax withheld
    stateTaxWheld     = []

    num = int(0)

    # Prompt for hours for the week and employee pay rates
    for num in range(ARRAY_SIZE):

        # Initialize sentinel value
        invalidHours = True

        # Start while loop
        while(invalidHours):  
            print("* EMPLOYEE ID      : ", employeeID[num])
            hoursPerWeek      = float(input("* Please enter hours worked: "))

            if hoursPerWeek > 60:
                print("Please enter a value less than 60 hours")
            else:
                # Set the hours per week for the current place in the hours worked array
                hoursWorkedArray.append(hoursPerWeek)
                invalidHours = False

        # Set the pay rate and prompt the user for value
        print("* EMPLOYEE ID      : ", employeeID[num])
        payRate           =  float(input("* Please enter the payrate: $"))
        payRateArray.append(payRate)

    # Re-initialize num
    num = 0
    
    # Begin for loop to calculate gross pay, fed and state tax
    for num in range(ARRAY_SIZE):
        grossPay = hoursWorkedArray[num]*payRateArray[num]
        grossPayArray.append(grossPay)

        fedTax = FED_TAX*grossPay
        fedTaxWheld.append(fedTax)

        stateTax = STATE_TAX*grossPay
        stateTaxWheld.append(stateTax)


    print("**************************************")
    print("      Output for Program          ")
    print("*************************************")
    num = 0

    for num in range(ARRAY_SIZE):
        print("* Employee ID  : ", employeeID[num])
        print("* Gross Pay    : $", grossPayArray[num])
        print("* Federal Taxes: $", fedTaxWheld[num])
        print("* State Taxes  : $", stateTaxWheld[num])
        print("-------------------------------------")

# Call main
main()
