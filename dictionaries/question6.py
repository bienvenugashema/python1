import question4

students = {
    'Sofiat': [56, 89, 70, 92, 67, 100],
    'Fionnuala': [60, 70, 100, 45, 70, 76],
    'Alex': [60, 95, 90, 85, 93, 45],
    'Ify': [55, 80, 56, 45, 51, 76],
    'JohnPaul': [78, 100, 65, 77, 91, 87],
    'Ben': [45, 78, 65, 50, 45, 87],
    'Tom': [32, 50, 45, 67, 40, 80]
}

# First way

sofiat = students['Sofiat']
question4.calculate_average(sofiat)

tom = students['Tom']
question4.calculate_average(tom)

# Second way

sofiat = students['Sofiat']
sum(sofiat)/len(sofiat)

tom = students['Tom']
sum(tom)/len(tom)

# Third way usin loop
sofiat1 = ""
tom1 = ""
for key, values in students.items():
    if key == "Sofiat":
        sofiat1 = sum(values)/len(values)
    if key == "Tom":
        tom1 = sum(values)/len(values)





