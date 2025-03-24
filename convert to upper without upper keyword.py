srt = input("text: ")
rf = str.maketrans("abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ")
text = srt.translate(rf)
print(text)