#This code demonstrates the creation of menus, franchises, and businesses
# and also provides methods to calculate bills and check available menus
#based on the current time.

#In the code, the classes represent a business that has multiple franchises,
#each with its own menus and each menu contains different food items with
#their prices and availability times. 

#Define a class named Business
class Business:

  #Initialize the Business object with a name and list of franchises
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises 

#Define a class named Franchise
class Franchise:
  
  #Initialize Franchise object with an address and list of menus
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  #Define a string representation for Franchise (prints its address)
  def __repr__(self):
    return self.address

  #Define a method to get available menus based on a specified time 
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

#Define a class named Menu
class Menu:

  #Initialize the Menu object with a name, items, start time, and end time 
  def __init__(self, name, items, start_time, end_time):
    self.name = name 
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  #Define a string representation for the Menu (prints its name & availability times)
  def __repr__(self):
    return self.name + " menu is available from " + str(self.start_time) + " - " + str(self.end_time) 

  #Define a method to calculate the bill based on purchased items
  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill



#Define a dictionary of brunch times and create a Menu object for brunch
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

brunch = Menu("brunch", brunch_items, 1100, 1600)

#Create more Menu objects for different meal options

#Define items for early bird menu
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}

early_bird = Menu("early bird", early_bird_items, 1500, 1800)

#Define items for dinner menu
dinner_items =  {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}

dinner = Menu("dinner", dinner_items, 1700, 2300)

#Define items for kids menu 
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids = Menu("kids", kids_items, 1100, 2100)

#print details of brunch menu
print(brunch)

#Calculate the bill for items from selected menus
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

#Create a list of menus
menus = [brunch, early_bird, dinner, kids]

#Create a flagship Franchise with a specific address and the list of menus 
flagship_store = Franchise("1232 West End Road", menus)

#Create another franchise with different address and same list of menus
new_installment = Franchise("12 East Mulberry Street", menus)

#Create a Business object with a name and a list of franchises
business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

#Create a dictionary of arepas items and create a Menu object for arepas
arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu("Take a' Arepa", arepas_items, 1000, 2000)

#Create Franchise for arepas business with address and the pertaining menu
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

#Create an arepas Buisness object with a name and the arepas franchise
arepa = Business("Take a' arepa", [arepas_place])

#Check the available menus at the flagship store at different times
print(flagship_store.available_menus(1200))

print(flagship_store.available_menus(1700))