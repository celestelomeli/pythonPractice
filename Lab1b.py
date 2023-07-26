#--------------------------------------------------------------
# Name: Maria Lomeli
# Date: October 20, 2021
# Reference: Assignment 1b for CISP 300
# Title: Customer info update
# Inputs: My name, birth city, birth year
# Process: Store the data in variables
# Outputs: Print stored data
#---------------------------------------------------------------
#Initialize variables        
FirstName = "Maria"          # Use your first name
LastName = "Lomeli"          # Use your last name 
City = "El Monte"            # Use your birth year
BirthYear = 0                # Initialize BirthYear

#Read in and store your birth year
BirthYear = int(input("Please enter your birth year: "))

#Print it all out
print("My name is: \t\t",FirstName, LastName)
print("My birth city is: \t", City)
print("My birth year is: \t", BirthYear)
                      
