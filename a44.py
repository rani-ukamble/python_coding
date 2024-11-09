# Assignment 44:

# Write a python function, remove_duplicates() which accepts a string and removes all duplicate characters from the given 
# string and return it.
# Also write the pytest test cases to test the program

# Sample Input                                        Expected Output
# 1122334455ababzzz@@@123#*#*                         12345abz@#*

from collections import Counter

def remove_duplicates(s):
    letter_freq = Counter(s)
    letter = letter_freq.keys()
    # freq = letter_freq.values()
    return ''.join(letter)

if __name__ == "__main__":
    s = input()
    ans = remove_duplicates(s)
    print(ans)