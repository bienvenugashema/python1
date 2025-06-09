l = [1,2,3]
r = [3,2,1]
new = []
d = list(zip(l, r))
for num in d:
    new.append(sum(num))
print(new)    
