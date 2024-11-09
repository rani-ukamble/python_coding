# 15 leap years starting from given year

year = int(input("Enter year: "))

cnt = 0

while cnt<15:
    year=year+1
    if (year%100==0 and year%400) or (year%100!=0 and year%4==0):
        print(year)
        cnt=cnt+1
