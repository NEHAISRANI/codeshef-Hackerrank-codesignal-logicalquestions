def calc(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '*':
        return a * b
    elif operator == '/': 
        return a / b
    elif operator == '-':
        return a - b
        
user=input("enter your numbe\n")
user1=input("enter your number\n")
user3=raw_input("enter your operator\n")
if ord(user3)>=42 and ord(user3)<=47:
    new=user3
else:
    print"check your operator"
result=(calc(user,user1,new) )
print(result) 