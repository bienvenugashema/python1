def missingNumber(arr):
    for number in range(1,len(arr) + 2):
        if number not in arr:
            print(number)
            
missingNumber([1,2,3,5,6,8,10,11])
