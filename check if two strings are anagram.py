def are_anagrams(str1, str2):
    arr1=[]
    arr2=[]
    if len(str1) == len(str2):
        
        for i in str1:
            arr1.append(i)

        for i in str2:
            arr2.append(i)
        arr1.sort()
        arr2.sort()
        if arr1 == arr2:
            return "are anagrams"
        else:
            return "Not anagrams"
    else:
        return"Not anagrams"


result = are_anagrams('listen','silent')
print(result)
