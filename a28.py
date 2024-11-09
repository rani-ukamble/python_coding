# Assignment 28:
 
# A 10-substring of a number is a substring of its digits that sum up to 10.
# For example, the 10-substrings of the number 3523014 are:
# 3523014, 3523014, 3523014, 3523014
# Write a python function, find_ten_substring(num_str) which accepts a string and returns the list of 10-substrings of that 
# string.
# Handle the possible errors in the code written inside the function.
# Sample Input Expected Output
# '3523014' ['5230', '23014', '523', '352'] 



def find_ten_substring(s, given_sum):
    l = []
    
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            currsum = sum(int(digit) for digit in substring)   
            if currsum==given_sum:
                l.append(substring)
    return l



if __name__ == "__main__":
    s = "3523014"
    given_sum = 10
    print(find_ten_substring(s, given_sum))