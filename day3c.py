# Challenge excercise


height = float(input("What is your height? (in meters) "))
weight = float(input("What is your weight? (in kgs) "))

bmi = weight / height ** 2

if bmi < 18.5:
    print(f"Your BMi is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your BMi is {bmi}, you are normal weight")
elif bmi < 30:
    print(f"Your BMi is {bmi}, you are slightly overweight")
elif bmi < 35:
    print(f"Your BMi is {bmi}, you are obese")
else:
    print(f"Your BMi is {bmi}, you are clinically obese")
