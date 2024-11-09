# Assignment 26:

# A vendor at a food court is in the process of automating his order management system.
# The vendor serves the following menu – Veg Roll, Noodles, Fried Rice and Soup and also maintains the quantity available for 
# each item. The customer can order any combination of items. The customer is provided the item if the requested quantity 
# of item is available with the vendor.
# Write a python program which implements the following functions.
# place_order(*item_tuple): This function accepts the order placed by the customer. Consider it to be a variable length 
# argument as each customer may have a different order.
# The function should check whether the items requested are present in the vendor‟s menu and if so, it should ccheck whether 
# the requested quantity is available for each by invoking the check_quantity_available() method.
# The function should display appropriate messages for each item in the order for the below scenarios:
# 1. When the requested item is not available in vendor‟s menu, display <Item Name> is not available
# 2. When the quantity requested by the customer is not available, display <Item Name> stock is over
# 3. When the requested quantity of the item is available with the vendor, display <Item Name> is available
# check_quantity_available(index,quantity_requested): This function should check whether the requested quantity of the 
# specified item is available. If so, it should reduce the quantity requested from the quantity available for that item and return 
# True. Otherwise, it should return False.
# Test your code by using the given sample inputs.
# Verify your code by using the 2
# nd sample input(highlighted) given below:

# Sample Input                                                      Expected Output
# Menu and quantity available                 Items Ordered
# (Veg Roll, Noodles, Fried Rice , Soup)      Veg Roll,2           Veg Roll is available
#                                             Noodles,2            Noodles is available
                                                
# [2,200,250,3]


# (Veg Roll, Noodles, Fried Rice , Soup)      Fried Rice,2
#                                             Soup,1
# [2,200,3,0]



def check_quantity_available(order, avail):
    for name in order:
        if name not in avail:
            print(name, "not available")
        else:
            if avail[name] >= order[name]:
                print(name, "is available")
            else:
                print(name, "stock is over")
                
if __name__ == "__main__":
    foodType = ("VegRoll", "Noodles", "FriedRice", "Soup")
    Menu_and_quantity_available = [2,200,3,0]
    food_avail = {}
    size = len(foodType)
    for i in range(size):
        food_avail[foodType[i]] = Menu_and_quantity_available[i]
    food_order = {}
    num_items = int(input("How many food items would you like to order? "))
    for i in range(num_items):
        food, quantity = input("Food type and quantity: ").split()
        food_order[food] = int(quantity)    
    check_quantity_available(food_order, food_avail)
