# Challenge - BMI calculator

# BMI = weight (kg) / (height ** 2) (m**2)

weight = input("What is your weight? ")
height = input("What is your height? ")


bmi = int(weight) / (float(height) ** 2)

print("Your BMI is: " + str(int(bmi)) + " kg/m^2")