n1=0
try:
    n=int(input("enter number: "))
except:
    print("plese enter integer")
else:
    if n<0:
        print("please enter positive number")
    else:
        while int(n)!=0:
            rem=int(n)%10
            n1=n1*10+rem
            n=int(n)/10
        print("reverse number = ",n1)
    
