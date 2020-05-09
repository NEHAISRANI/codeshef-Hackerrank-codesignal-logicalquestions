new=[]
i=0
while i<10:
    user=input("enter your number")
    new.append(user)
    i=i+1
j=0
c=new[1]-new[0]
k=1
while i<len(new)-1:
    if new[j]+c==new[k]:
        b="true"
    else:
        b="false"
        break
    j=j+1
    k=k+1
print(b)

