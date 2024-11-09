# AAAABBBBCCCCCCCC
# output 4A4B8C


# Method1

# input = input()
# output = ""
# cnt =1
# if not input:
#     print("-1")
# for i in range(1, len(input)):

#     if input[i]==input[i-1]:
#         cnt+=1
#     else:
#         output+= str(cnt)+input[i-1]
#         cnt=1

# output+= str(cnt)+input[-1]

# print(output)



# Method 2
input = input()

l=[]
cnt = 1
if not input:
    print("-1")
for i in range(1, len(input)):
    if input[i]==input[i-1]:
        cnt+=1
    else:
        l.append(str(cnt))
        l.append(input[i-1])
        cnt = 1

l.append(str(cnt))
l.append(input[-1])

ans = "".join(l)

print(ans)
