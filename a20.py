# Write a python program to display all the common characters between two strings. Return -1 if there are no matching 
# characters.
# Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.

# Sample Input 
# "I like Python"
# "Java is a very popular language"

# Expected output
# lieyon

s1 = input()
s2 = input()

s1 = s1.replace(" ", "")
s2 = s2.replace(" ", "")
ans = ""

if len(s1)>len(s2):
    for i in s2:
        if i in s1:
            ans+=i
else:
    for i in s1:
        if i in s2:
            ans+=i

print(ans)

