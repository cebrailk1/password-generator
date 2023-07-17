import string
import random

characters = list(string.ascii_letters + string.digits + "!§$%&/()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate a password? (Yes/No) : ")

if option == "Yes":
    generate_password()

elif option == "No":
    print("Passwordgenerator ended")
    quit()
else:
    print("Invalid input please try again")
    quit()