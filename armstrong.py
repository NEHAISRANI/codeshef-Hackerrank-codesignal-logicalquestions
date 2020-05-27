print("1")
i=150
while i<500:
    a=i
    sum=0
    while a>0:
        rem=a%10
        sum=sum+(rem**3)
        a=a//10
    else:
        if i==sum:
            print(i)
    i=i+1

        

# vowels = "aeiouAEIOU"
# consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
# v= 0
# const = 0
# a = input("enter the string ")
# i = 0 
# while i < len(a):
# 	w = "not vowel"
# 	j = 0
# 	while j < len(vowels):
# 		if a[i] == vowels[j]:
# 			v = v + 1
# 			w = "vowel"
# 			break 
# 		j = j + 1
# 	if w == "not vowel":
# 		k = 0
# 		while k < len(consonants):
# 			if a[i] == consonants[k]:
# 				const = const + 1
# 				break
# 			k = k + 1	
# 	i = i + 1
# print("vowels",v)
# print("constants",const)




