user=eval(input("enter your number"))
if user%5==0 and user%11==0:
    print("Both")
elif user%5==0:
    print("divisible by 5")
elif user%11==0:
    print("divisible by 11")
else:
    print("none")