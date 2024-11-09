# Write a function to find the medical speciality visited by the maximum number of patients and return the name of the 
# speciality.
# Also write the pytest test cases to test the program.
# Note:
# 1. Assume that there is always only one medical speciality which is visited by maximum number of patients.
# 2. Perform case sensitive string comparison wherever necessary.
# Sample Input Expected Output
# [101,P,102,O,302,P,305,P] Pediatrics



# solution

# n = int(input("Enter number of records : "))

# l=[]

# for i in range(n):
#     x = int(input())
#     y = input()
#     l.append(x)
#     l.append(y) 

# p =0
# o = 0
# e = 0

# for i in range(1, 2*n, 2):
#     if l[i]=='p':
#         p+=int(l[i-1])
#     elif l[i]=='o':
#         o+=int(l[i-1])
#     elif l[i]=='e':
#         e+=int(l[i-1])
#     else:
#         print("-1")

# maxi = max(p, o, e)
# if maxi==p:
#     print("Pediatrics")
# elif maxi == o:
#     print("Orthopedics")
# else:
#     print("ENT")
# print()


l = input("Enter record (format: '101,p,102,o,...'): \n").split(',')

# Initialize counters for each specialty
p = 0  # Pediatrics
o = 0  # Orthopedics
e = 0  # ENT

for i in range(1, len(l), 2):  
    speciality = l[i].strip().lower()  
    if speciality == 'p':
        p += int(l[i - 1]) 
    elif speciality == 'o':
        o += int(l[i - 1]) 
    elif speciality == 'e':
        e += int(l[i - 1]) 
    else:
        print("-1 (Invalid specialty)")  

maxi = max(p, o, e)
if maxi == p:
    print("Pediatrics")
elif maxi == o:
    print("Orthopedics")
else:
    print("ENT")
