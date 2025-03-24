def second_largest(lst):
    larg = 0
    larg1 = 0
    for n in lst:
        if n > larg:
            larg = n
    for n in lst:
        if n < larg:
            if n > larg1:
                larg1 = n
    print(larg1)
    

second_largest([1,4,2,3,6,8,5])    
