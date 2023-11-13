# Code challenge - Treasure map

line1 = ["__", "__", "__"]
line2 = ["__", "__", "__"]
line3 = ["__", "__", "__"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to hide the treasure? ")
letter = position[0].lower()
number= int(position[1]) - 1

abc = ["a", "b", "c"]
index = abc.index(letter)

map[index][number] = "x"

print(f"{line1}\n{line2}\n{line3}")