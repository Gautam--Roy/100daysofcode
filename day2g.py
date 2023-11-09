# Prject - Tip Calculator

print("Welcome to the tip calculator.\n")
total_bill = input("What was the total bill? $")
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
split_between = input("How many people to split the bill? ")

bill_split = (float(total_bill) * (1 + float(percentage_tip)/100)) / int(split_between)
bill_split = "{:.2f}".format(bill_split)

print(f"Each person should pay: ${bill_split}")