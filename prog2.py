# take comma separated string and list the positive and negative numbers from it

# s = input()
s = input("Enter comma separated numbers: ")
l= s.split(',')
for i in range(len(l)):
    l[i] = int(l[i])

neg = 0
pos = 0
for i in l:
    if int(i)<0:
        neg+=1
    elif int(i)>0:
        pos+=1

print(l)
print("Positive ", pos)
print("Negative ", neg)