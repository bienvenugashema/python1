def removeDouble(s):
    r=[]
    for i in range(0,len(s)):
        if s[i] != s[i - 1]:  # Check consecutive duplicates
            r.append(s[i])
    return ''.join(r)            

print(removeDouble("committee"))
