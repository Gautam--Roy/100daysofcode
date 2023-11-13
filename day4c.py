# Challenge code

import random


names = input("Enter the list of names: ")

name_list = names.split(", ")

if len(name_list):

    random_name = name_list[random.randint(0, len(name_list) - 1)]

    print(f"{random_name} is going to the pay the full bill")