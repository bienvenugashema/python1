def cammel_to_snake(text):
    arr = [i  for i in text]
    for i in arr:
        if i.isupper():
            arr[arr.index(i)] = '_'+i.lower()
    return ''.join(arr)            
           
