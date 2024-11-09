# Assignment 40:

# Write a python function,check_anagram() which accepts two strings and returns True, if one string is an anagram of 
# another string. Otherwise returns False
# The twostrings are considered to be an anagram if they contain repeating characters but none of the characters repeat at 
# the same position. The length of the strings should be the same.
# Also write the pytest test cases to test the program.

# Note: Perform case insensitive comparison wherever applicable.

# Sample Input                                                    Expected Output
# eat, tea                                                        True
# backward,drawback                                               False
#                                                                 (Reason: character 'a' repeats 
#                                                                 at position 6, not an anagram)
# Reductions,discounter                                           True
# About, table                                                    False



from collections import Counter

def check_anagram(s1, s2):
    if len(s1)!=len(s2):
        return False
    
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            return False
        
    if Counter(s1)!=Counter(s2):
        # tea ===> Counter({'t': 1, 'e': 1, 'a': 1})
        return False
    
    return True
    


if __name__ == "__main__":
    s1 = input("Enter s1: ")
    s2 = input("Enter s2: ")
    ans = check_anagram(s1, s2)
    print(ans)
