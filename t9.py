# Next Day of calender

day = int(input("Day : "))
month = int(input("Month : "))
year = int(input("Year : "))

if day==31 and month==12:
    day=1
    month=1
    year=year+1
elif (month==1 or month==3 or month==5  or month==7 or month==8 or month==10):
    if day<=30:
        day=day+1
    elif day==31:
        day=1
        month=month+1
elif (month==4 or month==6 or month==9  or month==11):
    if day<=29:
        day=day+1
    elif day==30:
        day=1
        month=month+1
elif month==2:
    if (year%100==0 and year%400) or (year%100!=0 and year%4==0):
        if day<=28:
            day=day+1
        elif day==29:
            day=1
            month=month+1
    else:
        if day<=27:
            day=day+1
        elif day==28:
            day=1
            month=month+1


print(f"{day} - {month} - {year}")

    

      
