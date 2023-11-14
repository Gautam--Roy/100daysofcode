# Code challenge

target = int(input("Enter a target number between 1 and whatever: "))

sum = 0
for number in range(1, target+1):
    if number % 2 == 0:
        sum += number

print(f"The sum of even number between 1 and {target} is: {sum}")



# Another variation using step

even_sum = 0
for number in range(1, target+1, 2):
    even_sum += number

print(f"The sum of even number between 1 and {target} using the step method is: {sum}")