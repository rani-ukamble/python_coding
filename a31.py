# Assignment 31:

# Write a python function find_duplicates(), which accepts a list of numbers and returns another list containing all the 
# duplicate values in the input list. If there are no duplicate values, it should return an empty list.
# Also write the pytest test cases to test the program.
# Sample Input Expected Output
# [12,54,68,759,24,15,12,68,987,758,25,69] [12, 68]


def find_duplicates(l):
    l.sort()
    ans = []
    for i in range(1, len(l)):
        if l[i] == l[i-1]:
            ans.append(l[i])
    return ans





if __name__ == "__main__":
    l = [12,54,68,759,24,15,12,68,987,758,25,69]
    ans = find_duplicates(l)
    print(ans)
    