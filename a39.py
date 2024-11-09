# Assignment 39:

# Assume that a poem is given. Write the regular expressions for the following:
# 1. Print how many times the letter 'v' appears in the poem.
# 2. Remove all the newlines from the poem and print the poem in a single line.
# 3. If a word has 'ch' or 'co', replace it with 'Ch' or 'Co'.
# 4. If the pattern has characters 'ai' or 'hi', replace the next three characters with *\*
# Test your code by using the given sample inputs.
# Verify your code by using the 2
# nd sample input(highlighted) given below:

# input:

# If I can stop one heart from breaking,
# I shall not live in vain;
# If I can ease one life the aching,
# Or cool one pain,
# Or help one fainting robin
# Unto his nest again,
# I shall not live in vain.

# output

# 4
# If I can stop one heart from breaking, I shall not live in vain; If I can ease one life the 
# aching, Or cool one pain, Or help one fainting robin Unto his nest again, I shall not live in 
# vain.
# If I can stop one heart from breaking,
# I shall not live in vain;
# If I can ease one life the aChing,
# Or Cool one pain,
# Or help one fainting robin
# Unto his nest again,
# I shall not live in vain.
# If I can stop one heart from breaking,
# I shall not live in vain;
# If I can ease one life the achi*\*
# Or cool one pain,
# Or help one fai*\*ng robin
# Unto hi*\*est again,
# I shall not live in vain.

import re


print("Enter poem: \n")
poem = []
while True:
    poemLine = input()
    if poemLine.strip().upper()=='END':
        break
    poem.append(poemLine)

currPoem = '\n'.join(poem)


# 1

print(poem.count('v'))
print()


# 2
poemIn1Line = currPoem.replace("\n", " ")
print(poemIn1Line)

print()


# 3
currPoem = currPoem.replace('ch', 'Ch')
currPoem = currPoem.replace('co', 'Co')
# print(currPoem)

print()

# 4

poem_modified = re.sub(r'(ai|hi)(.{3})', r'\1*\*', currPoem)
print(poem_modified)


