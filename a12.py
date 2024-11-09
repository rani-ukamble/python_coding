# Triangle sides or not

a = int(input("Enter side1: "))
b = int(input("Enter side1: "))
c = int(input("Enter side1: "))


maxi = max(a, b, c)
if maxi==a:
    if a<(b+c):
        print("side of triangle")
    else:
        print("not a side of triangle")
elif maxi==b:
    if b<(a+c):
        print("side of triangle")
    else:
        print("not a side of triangle")
else:
    if c<(b+a):
        print("side of triangle")
    else:
        print("not a side of triangle")
