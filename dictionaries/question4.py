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

empty = []

for values in temperatureCountries.values():
    empty.append(values)



Rwnda = [25, 33, 30, 21, 38, 29, 26, 27, 34, 23, 37, 31]
Kenya = [25, 33, 30, 21, 38, 29, 26, 27, 34, 23]

def calculate_average(lst: list) -> float:
    average = sum(lst)/len(lst)
    return average

average_rwanda = calculate_average(Rwnda)
average_kenya = calculate_average(Kenya)

temperatureCountries['Rwanda'] = average_rwanda
temperatureCountries['Kenya'] = average_kenya

# print(temperatureCountries)

