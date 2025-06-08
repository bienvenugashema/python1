def max_array(lst:list) -> float:
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

def min_array(lst: list) ->float :
    min_num = float('inf')
    for num in lst:
        if num < min_num:
            min_num = num
    return min_num

#To prinf max number

print(max_array([1,4,6,7,9,33,90,4]))

#To print min of array

print(min_array([1,4,6,7,9,33,90,4]))
