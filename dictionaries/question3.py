temperatureCountries = {
    'Rwanda': 29,
    'Nigeria': 28,
    'Kenya': 23,
    'Egypt': 37,
    'Morocco': 41,
    'SouthAfrica': 25,
    'Mali': 33,
    'Ghana': 28
}

for key, values in temperatureCountries.items():
    if values > 30 :
        print(f"{key} is Hot")
    elif values < 25:
        print(f"{key} is cold")
    print(f"{key}")       
