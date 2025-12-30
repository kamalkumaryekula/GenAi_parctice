
#menu items

import json
from pprint import pprint 


with open("C:/Users/Admin/OneDrive/Documents/menu_items.json") as f:
    data = json.load(f)

#pprint(data)

#Write a Python script to iterate through the menu data and print the name of each main menu 
#category. 
for item in data:
    pprint(item['name'])

'''['Appetizers',
 'Beverages',
 'Salads & Soups',
 'Entrees *',
 'Desserts',
 'Kids',
 'Oxford Menu',
 'DRINKS',
 'FOOD',
 'PIZZA',
 'Catering',
 'FISH']'''

#Extract and print the name of every menu item that belongs to the "Appetizers" category. 

for item in data:
    if item['name'] == 'Appetizers':
        for menuItem in item['menuItems']:
            print(menuItem['name'])

'''Blooming Onion
Buff Chkn Eggrolls
Buffalo Chkn Dip
Chicken Wings
Chili Bowl
Chips & Salsa
Chkn Quesadilla
Chkn Tender Bskt
Fried Mushrooms
Fried Pickles
Loaded Cheese Fries
Loaded Potato Skins
Mozzarella Sticks
Nachos
Spinach Artichoke Dip
Stuffed Banana Peppers'''


#Iterate through all non-alcoholic beverages and calculate their average price. The price can 
#be found under customConfigs as itemPrice. 

price = []
for A in data:
    if A['name'] == "Beverages":
        for B in A["subCategories"]:
            if B['name'] == "Non Alcoholic Beverages":
                for C in B['menuItems']:
                    price.append(C['customConfigs'][0]["itemPrice"])


avg = sum(price)/len(price)
print(avg)               #299.1666666666667
print(price)             #[299, 300, 299, 299, 299, 299]




