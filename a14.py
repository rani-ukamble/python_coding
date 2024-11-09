# head = rabbits + chicken
# legs = 4*rabbits + 2*chicken


heads = int(input())
legs = int(input())

rabbits = (legs - 2*heads)//2

chicken = heads - rabbits

if legs%2==1:
    print("No Solution")
else:
    print(f"Chicken = {chicken} \n Rabbits = {rabbits}  ")