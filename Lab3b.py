#----------------------------------------------------------------------
#This program was designed for a gas station that sells premium and regular gas. You are going 
#to calculate total sales for the month, total gas taxes collected and your 
#business’ income (total sales less gas taxes).
#----------------------------------------------------------------------
# Name:          Maria Lomeli
# Date:          November 6, 2021
# Reference:     A3b Lab
# Title:         Gas Income 
# Inputs:        User enters the following inputs: cost of premium gas per gallon,
#                cost of regular gas per gallon, number of premium gallons sold,
#                number of regular gallons sold, tax rate 
# Process:       Calculates total income for the gas station less the taxes on the gas
# Outputs:       The users input, premium gas income, regulare gas income, 
#                total sales, total taxes, total business income
#-----------------------------------------------------------------------

# Define main
def main():
    # Initialitize variable for premium gas cost per Gallon of gas
    premiumGasCost      = 0
    # Initialitize variable for egular gas cost per gallon of gas
    regularGasCost      = 0
    # Initialitize variable for premium gallons sold
    premiumGallonsSold  = 0
    # Initialitize variable for regular gallons sold
    regularGallonsSold  = 0
    # Initialitize variable for tax per gallon
    taxPerGallon        = 0
    #Initialize variable for premium income
    premiumIncome = 0
    #Initialize Variable for regular income
    regularIncome = 0
    # Initialize variable  for total business income
    totalBusinessIncome = 0

    # User Input Section
    premiumGasCost     = input("Please enter the cost of Premium Gas per Gallon: $")
    regularGasCost     = input("Please enter the cost of Regular Gas per Gallon: $")
    premiumGallonsSold = input("Please enter the premium Gallons Sold          :  ")
    regularGallonsSold = input("Please enter the regular Gallons Sold          :  ")
    taxPerGallon       = input("Please enter the tax rate                      : %")
    
    # calculate premium income
    premiumIncome = calculatePremiumIncome(float(premiumGasCost), float(premiumGallonsSold))
    # calculate regular income
    regularIncome = calculateRegularIncome(float(regularGasCost), float(regularGallonsSold))
    # calculate total business income
    totalBusinessIncome = businessIncome(regularIncome, premiumIncome, taxPerGallon)
    # display income report
    incomeReport(float(premiumGasCost), float(regularGasCost), premiumGallonsSold, regularGallonsSold, taxPerGallon, premiumIncome, regularIncome, totalBusinessIncome)
    
# calculate income for premium gas
def calculatePremiumIncome(premiumGasCost, premiumGallonsSold):
     return premiumGasCost * premiumGallonsSold

# calculate income for regular gas
def calculateRegularIncome(regularGasCost, regularGallonsSold):
    return regularGasCost * regularGallonsSold

# calculate total sales
def totalSales(regularIncome, premimumIncome):
    return regularIncome + premimumIncome

# calculate total taxes
def totalTaxes(totalSales, taxPerGallon):
    return totalSales * float(taxPerGallon)

# calculate the total income using total sales minus total taxes
def businessIncome(regularIncome, premiumIncome, taxPerGallon):
    totalSale = totalSales(regularIncome, premiumIncome)
    totalTax  = totalTaxes(totalSale, taxPerGallon)
    return totalSale - totalTax

# Income Report displays user input and calculations
def incomeReport(premiumGasCost, regularGasCost, premiumGallonsSold,
                 regularGallonsSold, taxPerGallon, premiumIncome, regularIncome, 
                 totalBusinessIncome):
    print("Premium Gas Cost             :$", premiumGasCost)
    print("Regular Gas Cost             :$", regularGasCost)
    print("Premium Gallons Sold         : ", premiumGallonsSold)
    print("Regular Gallons Sold         : ", regularGallonsSold)
    print("Premium Income               :$", premiumIncome)
    print("Regular Income               :$", regularIncome)
    print("Total Sales Less Taxes       :$", totalSales(regularIncome, premiumIncome))
    print("Total Taxes                  :$", totalTaxes(totalSales(regularIncome, premiumIncome), taxPerGallon))
    print("Total Business Income        :$", totalBusinessIncome)

# Call main
main()
