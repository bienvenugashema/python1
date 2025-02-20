import re
while True:
    password = input("Enter password: ")

    pattern = r"^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*]).+$"

    if re.match(pattern, password):
        print("Valid password")
    else:
        print("Invalid password")
