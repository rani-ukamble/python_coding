a1=int(input())
a5=int(input())
amt=int(input()) 


b5 = amt//5
r = amt%5 
if b5<=a5 and a1>=r:    
    print(f"{r},{b5}")
else:
    print("-1")
