# This program compares the cost of taking a trip in 2 different cars, 
# an Internal Combustion Engine car (ICEcar) and an electric car (eCar)
#----------------------------------------------------------------------
# Name:          Maria Lomeli
# Reference:     A2a Lab
# Title:         Car Compare
# Inputs:        User enters the following inputs: Distance, ICEcar MPG,
#                Cost of gallon of gas, eCar range, eCar full charge cost         
#                          
# Process:       Calculates and compares the cost of two car types: ICE vs
#                EV
# Outputs:       The users input, gallons of gas it will take for trip, 
#                the cost of the gas, charge count for eCar, cost of charging eCar,
#                determine cheaper car, difference in cost
#-----------------------------------------------------------------------
# Declare/Initialize the variables
# Declare & Initialize trip distance
tripDistance = 0.0
# Declare & Initialize ICEcar MPG
iceCarMpg = 0.0
# Declare & Initialize cost of gallon of gas
gasCost = 0.0
# Declare & Initialize eCar range
eCarRange = 0.0
# Declare & Initialize eCar full charge cost
eCarFullChargeCost = 0.0
# Declare & Initialize gallons of gas to complete the trip
gallonsOfGas = 0.0
# Declare & Initialize total trip gas cost
totalGasCost = 0.0
# Declare & Initialize total amount of charges required to complete trip
eCarChargeCount = 0.0
# Declare & Initialize total trip gas cost
electricityTotalCost = 0.0


# Prompt the user for distance of trip
tripDistance = float(input("Please enter trip distance in miles: "))

# Prompt the user for ICE car MPG
iceCarMpg = float(input("Please enter the MPG of the ICE Car: "))

# Prompt for cost of gallon of gas
gasCost = float(input("Please enter price of gas per gallon in dollars: $"))

# Prompt for eCar range
eCarRange = float(input("Please enter eCar range in miles: "))

# Prompt for eCar total charge cost
eCarFullChargeCost = float(input("Please enter eCar full charge cost in dollars: $"))

# Calculation for ICEcar gas cost 
gallonsOfGas = tripDistance / iceCarMpg
totalGasCost = gallonsOfGas * gasCost

# Calculation for eCar electricity cost 
eCarChargeCount = round(tripDistance / eCarRange)
electricityTotalCost = eCarChargeCount * eCarFullChargeCost

# Print user inputs
print("\nDistance of trip in miles:             ", tripDistance, " miles")
print("MPG of ICE Car:                        ", iceCarMpg)
print("Cost of gallon of gas:                $", gasCost)
print("ECar range:                            ", eCarRange, " miles")
print("eCar cost per charge:                 $", eCarFullChargeCost)
print("\nTotal ICECar cost of gas for trip:    $", totalGasCost)
print("Gallons of gas required for trip:      ", gallonsOfGas)
print("\nTotal ECar charge cost for trip:      $", electricityTotalCost)
print("ECar charges required for trip:        ", eCarChargeCount)

# Check if eCar fuel cost is less than ICEcar fuel cost
if (electricityTotalCost < totalGasCost):
    # Since eCar is cheaper print result and difference in cost
    print("\nThe E Car is cheaper to take.")
    difference = totalGasCost - electricityTotalCost
    print("The E car is $", difference, " cheaper than the ICE car.")
else:
    # Since ICE Car is cheaper print result and difference in cost
    print("\nThe ICE Car is cheaper to take")
    difference = electricityTotalCost - totalGasCost
    print("The ICE Car is $", difference, " cheaper to take than the eCar.")