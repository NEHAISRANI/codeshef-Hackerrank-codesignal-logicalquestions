# a = eval(input("enter number"))
# b = eval(input("enter number"))
# c = eval(input("enter number"))
# if a+b>c and b+c>a and c+a>b:
#     print("valid")
#     if a==b and a==c:
#         print("equilateral traingle")
#     elif a==b or a==c or b==c:
#         print("isoscelene triangle")
#     else:
#         print("scelene")
# else:
#     print("invalid")



# i=2
# count=1 
# while i<=100:
#     if i%2==0:
#         print (i)
#     if count==10:
#         break
#     i=i+2
#     count=count+1

# user=int(input())
# i=1
# while i<=10:
#     print(user*i)
#     i=i+1


n=int(input())
low=1
high = n+1
c=1
while c<=10:
    m=(low+high)/2
    c=c+1
    if m*m>n:
        high=m
        continue
    elif m*m==n:
        print (m)
        break
    else:
        low=m
        continue
print(m)