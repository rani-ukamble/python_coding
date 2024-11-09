# prod = [[1, "a", "INR 100", True], [2, "b", "INR 300", True]]

# # sum = 0
# # for i in range(len(prod)):
# #     l = prod[i][2]
# #     m = l.split()
# #     sum +=int(m[1])
# # print(sum)


# # 2
# count=0
 
# for i in range(0,len(prod)):
# 	price=int(prod[i][2].split()[1])
# 	count+=price
 
# print(count)

# # uppercase
# for i in range(0,len(prod)):
# 	prod[i][1] = prod[i][1].upper()
	
# print(prod)

# # prod.remove(prod[0])
# print(prod)


# # Add prod at index 1 and shift items from index 1
# prod.insert(1, [1, "c", "INR 600", True])
	
# print(prod)


# # 5% add at the end 

# # for i in prod:
# #     m = i[2].split()
# # 	m = int(m)
# # 	m+=int(m)*5/100
# # 	prod.append("INR ", )


# # Generator syntax---> Replace each item of list with its square
# lst = [1,3,4]
# lst = [item*item for item in lst ]
# print(lst)


# # Random list of size 10
# from random import random

# l = [int(round(random()*100, 0)) for i in range(1,10)]
# print(l)

	
	
# print random 5 even and 5 odd numbers in nested list as follow
# [[23, 4, 5, 7], [5,8,9]]

# from random import random

# output = [[], []]
# while True:
#     no = round(random()*100, 0)
#     if no%2==0 and len(output[0])<=4:
#         output[0].append(no)
#     else:
#         if len(output[1])<=4:
#             output[1].append(no)
# print(output)


p = [{"1": 6, 5: "hb", "jkhb": 900}, {"1": 6, 5: "hb", "jkb": 700}]

print(p)

for item in p:
    for value in item.values():
        if isinstance(value, int):  # Check if the value is an integer
            print(value)


