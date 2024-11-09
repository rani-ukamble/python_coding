# Assignment 21:
# Write a python function, find_pairs_of_numbers() which accepts a list of positive integers with no repetitions and returns 
# count of pairs of numbers in the list that adds up to n. The function should return 0, if no such pairs are found in the list.
# Also write the pytest test cases to test the program.
# Sample Input & Expected Output
# [1, 2, 7, 4, 5, 6, 0, 3], 6 --->3
# [3, 4, 1, 8, 5, 9, 0, 6], 9 --->4




# n = int(input("Enter size of list: "))
# for i in range(n):
#     x = int(input())
#     l.append(x)

# sum = int(input("Enter sum : "))

# Method 1 
def find_pairs_of_numbers(lst, target):
    seen = set()
    pairs = set()

    for i in lst:
        diff = target-i
        if diff in seen:
            pairs.add(tuple(sorted((i, diff))))
        else:
            seen.add(i)

    return len(pairs)


# Method 2
def find_pairs_of_numbers1(lst, target):
    lst.sort()
    l=0
    r=len(lst)-1
    cnt = 0
    while l<r:
        currsum = lst[l] + lst[r]
        if currsum == target:
            cnt+=1
            l+=1
            r-=1
        elif currsum > target:
            r-=1
        else:
            l+=1

    return cnt
        




if __name__ == "__main__":
    l = [3, 4, 1, 8, 5, 9, 0, 6, 2, 7]
    sum = 9
    if len(l)==len(set(l)):
        print(find_pairs_of_numbers1(l, sum))
    else:
        print("-1")
        
    # print(find_pairs_of_numbers(l, sum))
    # print(find_pairs_of_numbers1(l, sum))


