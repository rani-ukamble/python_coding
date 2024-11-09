# Assignment 33:

# Write a python function, nearest_palindrome() which accepts a number and returns the nearest palindrome greater than 
# the given number.
# Also write the pytest test cases to test the program.

# Sample Input        Expected Output
# 12300               12321
# 12331               12421

def nearest_palindrome(n):
    num = list(str(n))
    l = 0
    r = len(num)-1
    while l<r:
        if num[l]> num[r]:
            num[r] = num[l]
        elif num[l]< num[r]:
            num[r] = num[l]
        l+=1
        r-=1
    if int(''.join(num))>n:
        return int(''.join(num)) 
    l, r = (len(num)-1)//2, len(num)//2
    while l>=0:
        if num[l]!='9':
            num[l] = num[r] = str(int(num[l])+1)
            break
        else:
            num[l] = num[r] = '0'
        l-=1
        r+=1
    
    if num[0]=='0':
        num = ['1'] + ['0']*(len(num)-1) + ['1']   
    return int(''.join(num))

    

if __name__ == "__main__":
    n = 9009
    ans = nearest_palindrome(n)
    print(ans)