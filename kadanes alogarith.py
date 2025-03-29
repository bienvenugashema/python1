def find_sub_array(lst):
    max_sum= float('-inf')
    total=0
    for num in lst:
        total += num
        max_sum = max(max_sum,total)
        if total < 0:
            total = 0
    return max_sum

print(find_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
