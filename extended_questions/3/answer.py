def average_list(lst: list) -> float :
    total = 0
    for num in lst:
        total += num
    return f"Average is {total/len(lst)}"

print(average_list([1,2,3,4,5,6]))    