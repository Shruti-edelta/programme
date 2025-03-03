k=0
for i in range(1,6):
    k+=i
    for j in range(k,k-i,-1):
        print(j,end=" ")
    
    print()