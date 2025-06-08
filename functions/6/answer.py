def count_vowels(text):
    vowels = ['a', 'e', 'u', 'i', 'o']
    text = list(text.lower())
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return f"Total vowels are {count}" 

print(count_vowels("Bienvenu"))
       
