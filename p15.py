# whether no. is armstrong or not?

# 153 : Armstrong number

# Method 1
n = int(input())
p=n
sum = 0
while n>0:
    rem = n%10
    sum+=rem**3
    n= n//10

if sum==p:
    print("armstrong num")
else:
    print("not armstrong num")



# Method2
sum1=0
p =str(p)
for i in p:
    x= int(i)
    sum1+=x**3

if sum1==int(p):
    print("armstrong num")
else:
    print("not armstrong num")



# Caching - reg
# buffer memory - keyboard -RAM 

# Armstrong num

for i in range(153, 1001, 1):
    sum=0
    n = str(i)
    for j in n:
        x= int(j)
        sum+=x**3

    if sum==i:
        print(i)
