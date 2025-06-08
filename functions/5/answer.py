def count_occurance_of_char(text):
    text = list(text)
    dic = {}
    for char in text:
        dic[char] = f"{text.count(char)}"
    return dic    

print(count_occurance_of_char("Bienvenu"))