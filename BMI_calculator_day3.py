print("BMI Calculator")
height = float(input("Enter the height in m:"))
weight = int(input("Enter the weight in kg:"))

BMI = round(weight/height **2)
print(BMI)
print(f"The Body Mass Index of this Person is {BMI}")

if BMI < 18.5 :
    print(f"Your BMI is {BMI}, You are Underweight.")
elif BMI <= 25 :
    print(f"Your BMI is {BMI}, You are Normalweight.")
elif BMI <= 30 :
    print(f"Your BMI is {BMI}, You are Overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, You are obese.")
else:
    print(f"Your BMI is {BMI}, You are clinically obese.")
