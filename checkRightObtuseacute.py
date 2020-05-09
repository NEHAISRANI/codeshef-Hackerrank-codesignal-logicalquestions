 
s1 = eval(input("enter your number"))
s2 = eval(input("number"))
s3 = eval(input("number"))
if s1==90 or s2==90 or s3==90:
    print("right angle")
elif s1>90 or s2 > 90 or s3 > 90 :
    print("obtuse")
else:
    print("acute")
