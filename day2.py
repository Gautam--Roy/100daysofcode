# Data types

print(type("Gautam Roy")) # <class 'str'>
print(type(12323)) # <class 'int'>


num_char = len(input("What is your name? "))
new_num_char = str(num_char) # converting int to string
print("Your name has " + new_num_char + " characters")

print(7 + float("170.56"))