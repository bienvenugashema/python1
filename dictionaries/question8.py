countriesDict = {
    'Zimbabwe': {
        'capital': 'Harare',
        'population': 16,
        'neighbours': ['SouthAfrica', 'Botswana', 'Zambia', 'Mozambique'],
        'GDP': 41
    },
    'Rwanda': {
        'capital': 'Kigali',
        'population': 11,
        'neighbours': ['DRC', 'Uganda', 'Tanzania', 'Burundi'],
        'GDP': 30
    },
    'Nigeria': {
        'capital': 'Abuja',
        'population': 200,
        'neighbours': ['Cameroon', 'Benin', 'Chad', 'Niger'],
        'GDP': 1221
    },
    'Uganda': {
        'capital': 'Kampala',
        'population': 41,
        'neighbours': ['Rwanda', 'Kenya', 'Tanzania', 'Sudan', 'DRC'],
        'GDP': 102
    },
    'Kenya': {
        'capital': 'Nairobi',
        'population': 49,
        'neighbours': ['Tanzania', 'Uganda', 'Sudan', 'Somalia', 'Ethiopia'],
        'GDP': 190
    }
}


dictict = {
    'capital':"Daresalam",
    "population": 30,
    "neighbours": ['Rwanda','Kenya','Burundi','Uganda','Zimbabwe'],
    "GDP":300
}
countriesDict['Tanzani'] = dictict

# i

rwanda = countriesDict['Rwanda']
gdp = rwanda['GDP']

# ii_________________________________________________________________

zimbabwe = countriesDict['Zimbabwe']
capital = zimbabwe['capital']
# print(capital)

# iii__________________________________________________________

uganda = countriesDict['Uganda']
# by using list comphrehesion

neigbour = '\n'.join(n for n in uganda['neighbours'])

# by using for loop

for n in uganda['neighbours']:
    pass
    # print(n)

# iv________________________________________________________________________
input = input("Enter population value: ")
rwanda['population'] = input
# print(rwanda['population'])
print(countriesDict)

