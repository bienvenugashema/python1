import random
import string
while True:
    def generate_password(length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        return "".join((random.choice(characters))

        for _ in range(length))
    print("Generetaded password:", generate_password())
