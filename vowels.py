string="AaEeIiOoUu"
user="Chef IS coOking"

i=0
count=0
while i<len(user):
    j=0 
    while j<len(string):
        if user[i]==string[j]:
            count=count+1
        j=j+1 
    i=i+1
print("vowels=",count)
        