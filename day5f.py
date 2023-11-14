# Project - Password generator

import random

user_letters = int(input("How many letters would you like in your password? "))
user_symbols = int(input("How many symbols would you like in your password? "))
user_numbers = int(input("How many numbers would you like in your password? "))



letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '/', '?', '|', '\\']
selection = [letters, numbers, symbols ]


password = ""

for _ in range(0, user_letters):
    password += random.choice(letters)
for _ in range(0, user_symbols):
    password += random.choice(numbers)
for _ in range(0, user_numbers):
    password += random.choice(symbols)


password = [*password]
random.shuffle(password)

password = "".join(password)

print(f"The generated password is {password}")