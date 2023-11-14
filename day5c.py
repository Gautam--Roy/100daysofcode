#  For loop with the range function



for number in range(1, 10): # not including 10
    print(number)


for number in range(1, 11, 3): # last number is the step of increment
    print(number)

total = 0
for number in range(1, 101):
    total += number

print(total)