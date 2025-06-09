def multiples_of_three(lst:list)->int:
    count = 0
    for i in lst:
        if i % 3 == 0:
            count +=1
    return count

print(multiples_of_three([5, 6, 9, 10, 15, 17, 18, 21]))        