# Assignment 27:

# Write a recursive function, is_palindrome() to find out whether a string is a palindrome or not. The function should return true, if it is 
# a palindrome. Else it should return false.
# Note- Perform case insensitive operations wherever necessary.
# Also write the pytest test cases to test the program.


def is_palindrome(s):
    # base condition
    if len(s)<2:
        return True
    if s[0]!=s[-1]:
        return False
    return is_palindrome(s[1:-1]) #trimed string
    
    

if __name__ == "__main__":
    s = "abbbba"
    print(is_palindrome(s))

