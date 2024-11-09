# Assignment 22:

# A teacher is in the process of generating few reports based on the marks scored by the students of her class in a project 
# based assessment.
# Assume that the marks of her 10 students are available in a tuple. The marks are out of 25.
# Write a python program to implement the following functions:
# 1. find_more_than_average(): Find and return the percentage of students who have scored more than the average 
# mark of the class.
# 2. generate_frequency(): Find how many students have scored the same marks. For example, how many have 
# scored 0, how many have scored 1, how many have scored 3….how many have scored 25. The result should be 
# populated in a list and returned.
# 3. sort_marks(): Sort the marks in the increasing order from 0 to 25. The sorted values should be populated in a 
# list and returned.

# Sample Input 
# list_of_marks = 
# (12,18,25,24,2,5,18,20,20,21)

# Expected Output
# 70.0
# [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 2, 1, 0, 0, 1, 1]
# [2, 5, 12, 18, 18, 20, 20, 21, 24, 25]

def find_average(l):
    if len(l)==0:
        return False
    return sum(l)/len(l)

def find_more_than_average(l):
    avg = find_average(l)
    cnt=0
    for i in l:
        if i>avg:
            cnt+=1
    return cnt*100/len(l)

def generate_frequency(l):
    freq = [0]*26
    for i in l:
        freq[i]+=1
    return freq

def sort_marks(l):
    l = list(l)
    l.sort()
    return l
        


if __name__ == "__main__":
    l = (12,18,25,24,2,5,18,20,20,21)
    print(find_more_than_average(l))
    print(generate_frequency(l))
    print(sort_marks(l))
