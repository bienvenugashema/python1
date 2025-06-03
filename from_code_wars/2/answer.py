def are_you_playing_banjo(name):
    n = list(name.upper())
    if n[0] == "R":
        return name + " plays banjo"
    return name + " does not play banjo"    

print(are_you_playing_banjo("bienvenu"))  