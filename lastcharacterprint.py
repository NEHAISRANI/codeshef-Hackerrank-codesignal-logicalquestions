list1=["a", 1, "2", 5, "b", "q"]
user=input("enter your number")
a=len(list1)
i=a-user
while i<len(list1):
    print(list1[i])
    i=i+1

update user set authentication_string=PASSWORD("password") where User=("root")