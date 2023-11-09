# Challenge - Life in weeks

age = input("What is your current age? ")

age_in_int = int(age)

weeks_remaining = (90 - age_in_int) * 52


print(f"You have {weeks_remaining} weeks left")