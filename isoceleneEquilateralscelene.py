a = eval(input("enter number"))
b = eval(input("enter number"))
c = eval(input("enter number"))

if a==b and a==c:
    print("equilateral traingle")
elif a==b or a==c or b==c:
    print("isoscelene triangle")
else:
    print("scelene")

