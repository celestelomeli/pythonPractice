#----------------------------------------------------------------------
# This program calculates the total property tax on a home from the home 
#value, property tax rate and the .25% surcharge rate for each bedroom.
#----------------------------------------------------------------------
# Name:          Maria Lomeli
# Date:          November 6, 2021
# Reference:     A3a Lab
# Title:         Property Tax
# Inputs:        User enters the following inputs: home value, property 
#                tax rate, and number of bedrooms      
# Process:       Calculates the total property tax on a home           
# Outputs:       The users input, property tax, bedroom surcharge, 
#                total property tax
#-----------------------------------------------------------------------
# Define main
def main():
    # Declare/Initialize the variables
    homeValue = propertyTaxRate = numRooms = 0
    #Initialize variable - propertyTax calculated
    propertyTax      = 0
    # Initialize variable - bedroomSurcharge calculated
    bedroomSurcharge = 0
    # Initialize variable - totalPropertyTax cost calculated
    totalPropertyTax = 0

    # User inputs
    homeValue       = input("Please enter the value of the home                                :$")
    propertyTaxRate = input("Please enter the property tax rate as a value < 1 (i.e. 1% = 0.01):%")
    numRooms        = input("Please enter the number of rooms in the home                      : ")

    # call calcPropertyTax module
    propertyTax = calcPropertyTax(float(homeValue), float(propertyTaxRate))

    # call calcBedroomSurcharge module
    bedroomSurcharge = calcBedroomSurcharge(float(homeValue), int(numRooms))

    # call calcTotalPropertyTax module
    totalPropertyTax = calcTotalPropertyTax(float(propertyTax), float(bedroomSurcharge))

    # call displayTaxReport
    propertyTaxReport(homeValue, propertyTaxRate, numRooms, propertyTax, bedroomSurcharge, totalPropertyTax)

# Calculates property tax
def calcPropertyTax(homeValue, propertyTaxRate):
    return homeValue * propertyTaxRate

# Calculates bedroom surcharge
def calcBedroomSurcharge(homeValue, numRooms):
    return numRooms * .0025 * homeValue

# Calculates total property tax
def calcTotalPropertyTax(propertyTax, bedroomSurcharge):
    return propertyTax + bedroomSurcharge

# Displays user inputs and values calculated
def propertyTaxReport(homeValue, propertyTaxRate,
                     numRooms, propertyTax, 
                     bedroomSurcharge, totalPropertyTax):
    print ("\nProperty Tax Report")
    print("----------------------")
    print("Home Value                              :$", homeValue)
    print("Property Tax Rate                       :%", propertyTaxRate)
    print("Number of Rooms in home                 : ", numRooms)
    print("Property Tax Cost w/o bedroom surcharge :$", propertyTax)
    print("Bedroom Surcharge cost                  :$", bedroomSurcharge)
    print("Total Property Tax Cost                 :$", totalPropertyTax)

# call main function
main()
