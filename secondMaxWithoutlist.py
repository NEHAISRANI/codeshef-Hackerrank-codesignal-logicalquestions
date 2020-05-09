a=10
b=20
c=30
if a>b:
    if a>c:
        if b>c:
            print(b)
        else:
            print(c)
    else:
        print(a)
elif b>c:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>a:
        print(b)
    else:
        print(a)
