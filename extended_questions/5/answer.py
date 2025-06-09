lst = [1,1]

for num in range(51):
    for x in lst:
        add = lst[-1] + lst[-2]
    lst.append(add)    

print(lst)
