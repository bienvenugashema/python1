text = "python for bienvenu gashema"

#we want to reverse bienvenu

new = ''.join(i[::-1] for i in text.split() if i == "bienvenu")

print(text.replace("bienvenu", new))