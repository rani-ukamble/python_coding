level=int(input("Enter Levels "))
current_salary= int(input("Enter Current Salary: "))


if level==3:
    salary = current_salary+ ((current_salary*15)/100)
    print(f"salary= {salary} ")

 
elif level==4:
    salary = (current_salary*7)/100 + current_salary
    print(f"salary= {salary} ")
 
elif level==5:
    salary = (current_salary*5)/100 + current_salary
    print(f"salary= {salary} ")

else:
    print(f"salary= {current_salary} ")
    
 