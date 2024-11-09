
amt = 0
n = int(input("Enter no. of stone types you want: "))
if n<1:
    print("Enter quantity atleat 1")
    n = int(input("Enter no. of stone types you want: "))

for i in range(n):
    gemType = input("Gem type: ")
    gemType = gemType.lower()
    quantity = int(input("Enter quantity: "))

    if gemType=='a':
        cost=500
    elif gemType=='b':
        cost=400
    elif gemType=='c':
        cost=300
    else:
        cost=0
    amt+=cost*quantity
    
    


print(amt)