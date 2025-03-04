num_to_rom={1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC',100:'C',200:'CC',300:'CCC',400: 'CD',500: 'D',600:'DC',700:'DCC',800:'DCCC',900:'CM',1000: 'M'}

while True:
    n=input("enter number: ")
    if n.isnumeric():
        break
    else:
        continue
n=int(n)
ans=str()
if n<0 :
    print("please enter num between 1 to 5000")
else:
    while n!=0:
        t=n
        if len(str(n))==1:
            ans+=num_to_rom[t]
            n=t-n
        elif len(str(n))==2:
            n=n%10
            t=t-n
            # n=n-rem
            ans+=num_to_rom[t]
        elif len(str(n))==3:
            n=n%100
            t=t-n
            ans+=num_to_rom[t]
        else:
            com=10**(len(str(n))-1)
            print(com)
            n=n%com
            t=t-n
            if t in num_to_rom:
                ans+=num_to_rom[t]
            else:
                multy=int(t)/com
                for _ in range(int(multy)) :
                    ans+=num_to_rom[1000]


print("roman number : ",ans)
# MMMMMMCCLXXIII MMMMMMMMMCMXCIX


#  MMMMMMMMMMMMMMMMMMCMXCIX  99999
# MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMCMXCIX