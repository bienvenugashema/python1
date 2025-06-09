def runner_up(lst:list)->float:
    lrg1=lst[0]
    for num in lst:
        if num > lrg1:
            lrg1 = num
    lrg2 = float('-inf')
    for num in lst:
        if num > lrg2 and num < lrg1:
            lrg2 = num
    return lrg2        

print(runner_up([2, 3, 3, 6, 4, 5]))