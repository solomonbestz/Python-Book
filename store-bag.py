# STORE BAG PROGRAM

"""
This is the full code version of our store bag program
The store bag would have features like
Lists of bags available
price tags on bag brand
quanity available
add bag, price, and quantity
quantity below 0 => out of stock
"""
bag_brand = {"BackPack": [0, 2900.00, False], "BeltBag": [3, 4500.00, False], "Bindle": [4, 3100.00, False], "Box-Clutch": [4, 7000.00, False]}



def check_stock(bag_quantity):
    if bag_quantity == 0:
        bag_brand["BackPack"][2] = True
    

check_stock(bag_brand["BackPack"][0])
print(bag_brand)



print(bag_brand["BackPack"][1])

