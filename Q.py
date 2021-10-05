number=input("enter the number")
a=len(number)-2
b=int(number)//10**a
c=b%10
if c==3:
    print("yes")
else:
    print("no")