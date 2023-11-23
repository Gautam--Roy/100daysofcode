programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A peice of code that you can easily run over and over again",
}

# Reading from dictionary
bug = programming_dictionary["Bug"]

# Adding to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

# Empty a dictionary
empty_dictionary = {}

# Wipe a dictionary
# programming_dictionary = {}


# Edit an item in a dictionary
programming_dictionary["Bug"] = "A new definition"


# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
