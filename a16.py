# The road transport corporation (RTC) of a city wants to know whether a particular bus-route is running on profit or loss.
# Assume that the following information are given:
# Price per litre of fuel = 70
# Mileage of the bus in km/litre of fuel = 10
# Price(Rs) per ticket = 80
# The bus runs on multiple routes having different distance in kms and number of passengers.
# Write a function to calculate and return the profit earned (Rs) in each route. Return -1 in case of loss.

dist = int(input("Distance : "))
num_Passangers = int(input("num_Passangers : "))

fuel_cost = 70*dist//10
revenue = num_Passangers*80

if revenue>fuel_cost:
    print("Profit = ", revenue-fuel_cost)
elif revenue<fuel_cost:
    print("-1")




