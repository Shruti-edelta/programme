# n1=0
# try:
#     n=int(input("enter number: "))
# except:
#     print("plese enter integer")
# else:
#     if n<0:
#         print("please enter positive number")
#     else:
#         while int(n)!=0:
#             rem=int(n)%10
#             n1=n1*10+rem
#             n=int(n)/10
#         print("reverse number = ",n1)
    
n1=0
while True:
    n=input("enter number: ")
    if n.isnumeric():
        break
    else:
        print("str")
        continue
if int(n)<0:
   print("please enter positive number")
else:
    # while int(n)!=0:
    #     rem=int(n)%10
    #     n1=n1*10+rem
    #     n=int(n)/10
    # print("reverse number = ",n1)
    for i in range(len(n)-1,-1,-1):
        print(n[i],end="")
