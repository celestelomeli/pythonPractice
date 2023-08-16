# Arc Auto Sales is a new car dealership that sells BMWs, Toyotas, Hyundais
# and Chevys, and has 3 salespersons on site. You are going to open the 
# provided sales.dat file, read the records from the file, and print out 
# a sales report. 
print ("""
#---------------------------------------------------------------
# Name:         Maria Lomeli
# Date:         December 10, 2021
# Reference:    Chapter 10, Lab 8a
# Title:        File
# Inputs:       File sales.dat containing sales data
# Process:      Open, read and sum file of sales data
# Outputs:      Print title of sales report, total car brand sold, total
#               of each car model, total each salesperson sold, total
#               cost of cars sold by each salesperson 
#---------------------------------------------------------------
""")
def main():

    # Initialize and Declare variable
    count           = 0

    # Initialize and Declare Sales Report Variables
    patTotalSales   = 0
    danaTotalSales  = 0
    averyTotalSales = 0
    patTotalUnits   = 0
    danaTotalUnits  = 0
    averyTotalUnits = 0
    calcTotalSales  = 0
    salesList       = []

    unitsM340i           = 0
    units530e            = 0
    unitsM550i           = 0
    unitsX6              = 0
    unitsCorvette        = 0
    unitsSilverado       = 0
    unitsTucson          = 0
    unitsPalisade        = 0
    unitsVeloster        = 0
    unitsCorolla         = 0
    unitsCamry           = 0
    unitsRav4            = 0
    units4Runner         = 0 
    unitsTundra          = 0

    # Initialize and Declare Car data
    bmwSales        = 0
    chevySales      = 0
    toyotaSales     = 0
    hyundaiSales    = 0
    bmwUnits        = 0
    chevyUnits      = 0
    toyotaUnits     = 0
    hyundaiUnits    = 0


    # Initialize and declare variables for sales entry 
    salesPerson = ""
    make        = ""
    model       = ""
    price       = 0
    salesEntry = [salesPerson, make, model, price]

# Declare input file with "sales. dat" and mode 
    infile = open("sales.dat", 'r')

#******************************************    
    #saleslist = list(infile.readlines())
#***************************************
   # print ("Length of numlist =", len(saleslist), "\n")
    #print("Sales list: ", saleslist)

# Use a for loop to split up the indexes in salesEntry list 
    for line in infile:
        # Use splitlines() method to split string into a list 
        splitLine = line.split(",")
        salesEntry = [ str(splitLine [0]), str(splitLine [1]), str(splitLine [2]), int(splitLine [3])]
        #print("Data read in is: ", salesEntry)
        # Append salesEntry split data into empty salesList
        salesList.append(salesEntry)
  
  # Use for loop to print and iterate through salesList 
    for count in range(len(salesList)):
        print(salesList[count][0],":",salesList[count][1],",",salesList[count][2],",",salesList[count][3])
      # if index count in list matches listed matcg, append price to sales person's total sales and keep track 
      # of total cars (units) sold by each sales person
        if salesList[count][0].strip() == "Pat":
            patTotalSales = patTotalSales + salesList[count][3]
            patTotalUnits = patTotalUnits + 1
        elif salesList[count][0].strip() == "Dana":
            danaTotalSales = danaTotalSales + salesList[count][3]
            danaTotalSales = danaTotalUnits + 1
        elif salesList[count][0].strip() == "Avery":
            averyTotalSales = averyTotalSales + salesList[count][3]
            averyTotalUnits = averyTotalUnits + 1
        else:
            print("Error finding a match for the sales person name")

  #if second index (make) matches certain car, append total to each car variable [car]Units
  # print error if no match
        if salesList[count][1] == "BMW":
            bmwUnits = bmwUnits + 1 

            if salesList[count][2] == "M340i":
                unitsM340i = unitsM340i + 1
            elif salesList[count][2] == "530e":
                  units530e = units530e + 1
            elif salesList[count][2] == "M550i":
                unitsM550i = unitsM550i + 1
            elif salesList[count][2] == "X6":
                unitsX6 = unitsX6 + 1
            else:
                print("Error in BMW model selection")
        elif salesList[count][1] == "Chevy":
            chevyUnits = chevyUnits + 1

            if salesList[count][2] == "Corvette":
                unitsCorvette = unitsCorvette + 1
            elif salesList[count][2] == "Silverado":
                unitsSilverado = unitsSilverado + 1
            else:
                print("Error in Chevy model selection")
        elif salesList[count][1] == "Hyundai":
            hyundaiUnits = hyundaiUnits + 1

            if salesList[count][2] == "Tucson":
                unitsTucson = unitsTucson + 1
            elif salesList[count][2] == "Palisade":
                unitsPalisade = unitsPalisade + 1
            elif salesList[count][2] == "Veloster":
                unitsVeloster = unitsVeloster + 1
            else:
                print("Error in Hyundai model selection")
        elif salesList[count][1] == "Toyota":
            toyotaUnits = toyotaUnits + 1

            if salesList[count][2] == "Corolla":
                unitsCorolla = unitsCorolla + 1
            elif salesList[count][2] == "Camry":
                unitsCamry = unitsCamry + 1
            elif salesList[count][2] == "Rav4":
                unitsRav4 = unitsRav4 + 1
            elif salesList[count][2] == "4Runner":
                units4Runner = units4Runner + 1
            elif salesList[count][2] == "Tundra":
                unitsTundra = unitsTundra + 1
            else:
                print("Error in Toyota model selection")

    #print output (title of report, total car brand sold, total of each car model sold, total of cars 
    # each salesPerson sold, cost of cars sold by each sales person)
    print("******************************************************")
    print("*            Car Sales Reporting System              *")
    print("*                                                    *")
    print("******************************************************")
    print("CAR MAKE DETAILS")
    print("-----------------------")
    print("Chevy Sales                 : ", chevyUnits)
    print("BMW Sales                   : ", bmwUnits)
    print("Hyundai Sales               : ", hyundaiUnits)
    print("Toyota Sales                : ", toyotaUnits)
    print("--")
    print("CAR MODEL DETAILS")
    print("-----------------------")
    print("BMW")
    print("--")
    print("M340i:", unitsM340i)
    print("530e:", units530e)
    print("M550i:", unitsM550i)
    print("X6:", unitsX6)
    print("--")
    print("Chevy")
    print("--")
    print("Corvette:", unitsCorvette)
    print("Silverado:", unitsSilverado)
    print("--")
    print("Hyundai")
    print("--")
    print("Tucson:", unitsTucson)
    print("Palisade:", unitsPalisade)
    print("Veloster:", unitsVeloster)
    print("--")
    print("Toyota")
    print("--")
    print("Camry:", unitsCamry)
    print("Corolla:", unitsCorolla)
    print("Rav4:", unitsRav4)
    print("4Runner:", units4Runner)
    print("Tundra:", unitsTundra)
    print("EMPLOYEE SALES DETAILS")
    print("-----------------------")
    print("SALESPERSON 1")
    print("---")
    print("Pat Total Sales Amount      : ", patTotalSales)
    print("Pat Total Units Sold        : ", patTotalUnits)
    print("---")
    print("SALESPERSON 2")
    print("---")
    print("Dana Total Sales Amount     :", danaTotalSales)
    print("Dana Total Units Sold       :", danaTotalUnits)
    print("---")
    print("SALESPERSON 3")
    print("---")
    print("Avery Total Sales Amount    :", averyTotalSales)
    print("Avery Total Units Sold      :", averyTotalUnits)
    print("END OF REPORT")
    print("***********************************************")

#Close the file 
    infile.close()
#Call main 
main()
