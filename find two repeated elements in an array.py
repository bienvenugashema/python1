def twice(arr):
    for i in set(arr):
        if arr.count(i) > 1:
            print(i)

twice([1,2,3,4,5,4,6,7,3])          
