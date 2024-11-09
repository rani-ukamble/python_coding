# Write a python program which finds the maximum number from num1 to num2 (num2 inclusive) based on the following 

# rules.
# 1. Always num1 should be less than num2
# 2. Consider each number from num1 to num2 (num2 inclusive). Populate the number into a list, if the below 
# conditions are satisfied
# a. Sum of the digits of the number is a multiple of 3
# b. Number has only two digits
# c. Number is a multiple of 5
# 3. Display the maximum element from the list
# In case of any invalid data or if the list is empty, display -1.

l = []

n1 = int(input("n1 : "))
n2 = int(input("n2 : "))

if n1<n2:
    for i in range(n1, n2+1):
        sum=0
        temp = i
        if len(str(temp))==2 and temp%5==0:
            
            while i>0:
                r=i%10
                sum+=r
                i//=10
            if sum%3==0:
                l.append(temp)

if len(l)==0:
    print("-1")
else:
    maxi = max(l)
    print(f"Maximum element = {maxi}")
    
