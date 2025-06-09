def count_ints(lst:list):
    dic = {'Positive':0, "Negative": 0, "Zeros": 0}
    for nums in lst:
        if nums > 0:
            dic['Positive'] +=1
        if nums < 0:
            dic['Negative'] += 1
        if nums == 0:
            dic['Zeros'] += 1
    return dic             



lis = [1,2,3,4,-3,-2,-8,0,1]
print(count_ints(lis))
