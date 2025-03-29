def fizz_buzz(start,end):
    arr = [i for i in range(start,end+1)]
    for i in arr:
        if i % 3==0 and i % 5 ==0:
            arr[arr.index(i)] = "FizzBuzz"
        elif i % 3 == 0:
            arr[arr.index(i)] = "Fizz"
        elif i % 5 == 0:
            arr[arr.index(i)] = "Buzz"
    return arr        


print(fizz_buzz(1,30))       
