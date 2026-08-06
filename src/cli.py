import getpass
from generator import passwordGen

def home_menu():
    print("[G]et, [C]reate, [Q]uit")
    return input("Choose a valid input: ")

def prompt_add():
    service = input("Enter service name: ")
    pass_opt = input("Generate password? (y/n)")

    if pass_opt.lower() == "y":
        gen = passwordGen()
        password = gen.password
        return service, password

    elif pass_opt.lower() == "n":
        password = getpass.getpass("Enter password: ")
        return service, password

def prompt_get():
    return input("Enter service name: ")