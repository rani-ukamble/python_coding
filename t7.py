food_type = input("Enter food_type 'v' for veg and 'n' for non-veg : ")
quantity = int(input("Enter quantity of food : "))
dist = int(input("Enter distance : "))


if food_type=='v':
    cost = 120
elif food_type=='n':
    cost = 150
else:
    print("-1")

if dist<=3:
    delievery_charge=0
elif dist<=6:
    delievery_charge=(dist-3)*3
else:
    delievery_charge=(dist-3)*6+9

total_cost = cost*quantity+delievery_charge

print("total_cost = ",total_cost )



