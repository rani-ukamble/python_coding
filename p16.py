# Program to input bracket sequence and validate whether the sequence is valid or not
# {()}[]<>

b = input("Enter bracket sequence: ")

stack = []
for i in b:
    if i in '{[(<':
        stack.append(i)
    else:
        if not stack:  # Check if the stack is empty
            print("Invalid")
            break

        curr = stack[-1]
        if (i == '}' and curr == '{') or (i == ']' and curr == '[') or (i == ')' and curr == '(') or (i == '>' and curr == '<'):
            stack.pop()
        else:
            print("Invalid")
            break
else:
    # If we finish the loop without a break
    if stack:  # If the stack is not empty, it's invalid
        print("Invalid")
    else:
        print("Valid")
