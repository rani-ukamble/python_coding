# Assignment 35:

# Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
# The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.
# The function should identify the degree of correctness as mentioned below:
# CORRECT, if it is an exact match
# ALMOST CORRECT, if no more than 2 letters are wrong
# WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.
# and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG 
# answers.
# Assume that the words contain only uppercase letters and the maximum word length is 10.
# Also write the pytest test cases to test the program.

# Sample Input 
# {"THEIR": "THEIR", "BUSINESS": 
# "BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}

# Expected Output
# [2, 2, 1]


def find_correct(d):
    l=[]
    CORRECT, ALMOST_CORRECT, WRONG = 0, 0, 0
    for key, val in d.items():
        cnt=0
        if len(key)!=len(val):
            WRONG+=1
        else:
            for i in range(len(key)):
                if key[i]!=val[i]:
                    cnt+=1
            if cnt == 0:
                CORRECT+=1
            elif cnt<=2:
                ALMOST_CORRECT+=1
            else:
                WRONG+=1
  
    return [CORRECT,ALMOST_CORRECT, WRONG ]

if __name__ == "__main__":
    dict = {"THEIR": "THEIR", "BUSINESS": "BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR", "SAMPLE":"SAMPLE"}
    ans = find_correct(dict)
    print(ans)