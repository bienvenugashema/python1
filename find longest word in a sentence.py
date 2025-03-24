def longest(text):
    arr = text.split()
    count=""
    for sentence in arr:
        if len(sentence) > len(count):
            count = sentence
    return count        
                    

print(longest("mwimule bienvenu numunyeshuri wiga mucyigo cyisunze"))    
