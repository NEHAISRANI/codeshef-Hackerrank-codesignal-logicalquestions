new=[]
i=1
while i<=5:
    user=input("enter your name")
    new.append(user)
    i=i+1 
length=len(new)
index=length-1
while index>= 0:
    print(new[index])
    index=index-1 