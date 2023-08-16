#--------------------------------------------------------------------------------------
# This program calculates the total cost of a highway construction project based on
# predetermined costs for each terrain type with discountedPrices applied bases on miles 
# entered for each terrain type in the construction project. 
#---------------------------------------------------------------------------------------
# Name:          Maria Lomeli
# Date:          November 13, 2021
# Reference:     A4b Lab
# Title:         Highway Construction Cost 
# Inputs:        Mountainous miles to build, coastal miles to build, and flatland miles
#                to build
# Process:       Calculates total cost of a highway construction project     
# Outputs:       The users input and total cost for each terrain type
#----------------------------------------------------------------------------------------
# Set global variables
# Coast for each terrain in US Dollars
MOUNTAINOUS = 50000.00
COASTAL     = 40000.00
FLATLAND    = 25000.00  

#Define main
def main():
    # Declare/Initialize the variables
    # Amount of mountain road in miles to build
    mountainousMiles = 0.0
    # Amount of coastal road in miles to build
    coastalMiles     = 0.0
    # Amount of coastal road in miles to build
    flatlandMiles    = 0.0
    
    # Get User input for processing
    mountainousMiles = input("Please enter mountainous miles to build  :")
    coastalMiles     = input("Please enter the costal miles to build   :")
    flatlandMiles    = input("Please enter the flatland miles to build :")

    # Call ProjectCostRepot module
    ProjectCostReport(mountainousMiles, coastalMiles, flatlandMiles)

# determine discounted price given miles to be build
def calcPercentDiscount(miles):
    if (miles >= 2 and miles <= 10):
        return .10
    elif (miles >= 11 and miles <= 50):
        return .20
    elif (miles > 50):
        return .30
    else:
        return 0

# calculate discounted price cost per mile given the terrain type
def calcDiscMileCost(miles, terrain):    
    if(terrain == "mountainous"):
        return MOUNTAINOUS - (MOUNTAINOUS*calcPercentDiscount(float(miles)))
    elif(terrain == "coastal"):
        return COASTAL - (COASTAL*calcPercentDiscount(float(miles)))
    elif(terrain == "flatland"):
        return FLATLAND - (FLATLAND*calcPercentDiscount(float(miles)))
    else:
        print("Error, terrain type does not exist")
        return 0

# Calculate total cost to build highway for each terrain
# given miles and discounted miles cost
def costPerTerrainType(miles, discountedPrice):
    return int(miles) * float(discountedPrice)
    
# Calculates and prints total project cost given total cost for each terrain type  
def ProjectCostReport(mountainousMiles, coastalMiles, flatlandMiles):
    # Initialize local variables
    totalProjectCost = 0
    totalMountainous = 0
    totalCoastal     = 0
    totalFlatland    = 0

    # Print message to user
    print("\nUser Input")
    print("----------")
    print("Mountainous Miles  : ", mountainousMiles)
    print("Coastal Miles      : ", coastalMiles)
    print("Flatland Miles     : ", flatlandMiles)
    
    print("\nCalculations")
    print("------------")

    # Calculations
    # call costPerTerrain(miles, calcDiscMileCost(miles, "terrainType")) to get total cost for each terrain
    totalMountainous = costPerTerrainType(mountainousMiles, calcDiscMileCost(mountainousMiles, "mountainous"))
    totalCoastal     = costPerTerrainType(coastalMiles, calcDiscMileCost(coastalMiles, "coastal"))
    totalFlatland    = costPerTerrainType(flatlandMiles, calcDiscMileCost(flatlandMiles, "flatland"))
    totalProjectCost = totalMountainous + totalCoastal + totalFlatland
    print("Total Mountainous Cost: $", totalMountainous)
    print("Total Coastal Cost    : $", totalCoastal)
    print("Total Flatland Cost   : $", totalFlatland)
    print("-------------------------")
    print("Grand Total           : $", totalProjectCost)


#Call main
main()
