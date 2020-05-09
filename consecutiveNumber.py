i=0
new=[]
while i<7:
    user=input("enter your number")
    new.append(user)
    i=i+1

index = new[0] 
index=index+1
i = 1
while i<len(new):
    if index==new[i]:
        index=index+1
        i=i+1
    else:
        print(False)
        break
else:
    print(True)
        