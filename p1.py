# num_to_rom={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}

num_to_rom={1:'I',2:'II',3:'III',4:'IV',5:'V',10:'X'}
n=int(input("enter number: "))
r=str()
if n<0 and n>=20:
    print("please enter num between 1 to 20")
else:
    if n in num_to_rom:
        r+=num_to_rom[n]

print("roman number : ",r)
        

    


