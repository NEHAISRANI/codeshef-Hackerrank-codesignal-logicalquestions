def truncateString(str, num) :
    i=0
    count=0
    string=""
    while i<len(str):
        string+=str[i]
        count=count+1
        if count==num:
            string=string+"..."
            break
        i=i+1
    print(string)
 


truncateString("A-tisket a-tasket A green and yellow basket", 8);
