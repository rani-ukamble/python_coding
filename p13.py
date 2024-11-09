m = int(input("m: "))
n = int(input("n: "))

# for i in range(m, n+1,1):
#     if i%2==0:
#         print(i, end="\t")
# print("count ", (n-m)//2)

print("Odd : ")
for i in range(m, n, 2):
    if i%2==1:
        print(i, end="\t")
print("count ", (n-m)//2)


# print("Even : ")
# while m<=n:
#     if m%2==0:
#         print(m, end="\t")
#         m+=1

# print("Odd : ")

# while m<=n:
#     if m%2==1:
#         print(m, end="\t")
#         m+=1
  