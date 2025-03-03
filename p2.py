
# roman_numerals = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"V":5,"IV":4,"I":1}
roman_numerals = {"L":50,"XL":40,"X":10,"V":5,"IV":4,"I":1}

n=input("enter roman number: ")
n=n.upper()
int=0
for i in range(len(n)):
    try:
        if n[i] in roman_numerals:
            if len(n)>i+1 and roman_numerals[n[i]]<roman_numerals[n[i+1]]:
                int-=roman_numerals[n[i]]
            else:
                 int+=roman_numerals[n[i]]
        else:
            break
    except:
        print("not valid roman number")

print("integer=",int)