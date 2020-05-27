i=0
z=1
while i<25:
    j=z
    if j%2==1:
        while j<=i+5:
            print (j,"",end="")
            j=j+1
        z=j+4
    else:
        while j>=z-4:
            print (j,"",end="")
            j=j-1
        z=j+6 
    print("\n")
    i=i+5 


