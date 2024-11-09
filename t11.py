gender=input("Enter gender: ")
age = int(input("Enter age: "))
amt=int(input("Enter amount: "))

if 25<=age<=65 :
    if gender=='m':
        if amt>200000:
            print("Premium will be (amt/1000)*6 per thousand")
        elif 10000<amt<=200000:
            print("Premium will be (amt/1000)*2 percent of policy amount")
        
    elif gender=='f':
        if amt>100000:
            print("Premium will be (amt/1000)*3 per thousand")

else:
    print("not eligible")