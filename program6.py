#WAP to input any 5 digit number. replace its last digit with product
#of first and last digit.   example: no = 48579 then output = 485736


no = int(input("Enter 5 digit number :"))


#method-1
ans = (no//10)*100 + (no//10000)*(no%10) #485736
print("Ans = ",ans)

x = str(no) # "48579"
print("x[0] = ",x[0])           #"4"
print("x[-1] = ", x[-1])        #"9"
print("x[0:4] = ", x[0:4])      #"4857"
print("x[:4] = ", x[:4])        #"4857"
print("x[:] = ", x[:])          #"48579"
print("x[-3:] = ", x[-3:])      #"579"
print("x[:-3] = ", x[:-3])      #"48"


#method-2
ans = int(x[:-1] + str(int(x[0])*int(x[-1])))

print("ans = ", ans)
