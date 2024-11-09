from math import ceil

s = int(input())

if s>150:
    snacks = 40*s
else:
    snacks = 50*s

if s>100:
    # cost=2*2000
    cost = ceil(s/100)*2000
else:
    cost=2000

print("Transportation cost: ", cost)
print("snacks cost: ", snacks)



