# Lists


new_zealand = ["Wellington", "Auckland", "Napier", "Tauranga"]


print(new_zealand[2])
print(new_zealand[-1]) # Negative indices. Starts from last item.

new_zealand[2] = "Hamilton"

print(new_zealand[2])


new_zealand.append("Palmerston North") # Add to the list
new_zealand.extend(["Whangarei", "Taranaki"]) # Add to the list


print(new_zealand)