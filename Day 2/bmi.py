# # 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height = float(height)
weight = float(weight)
bmi =  weight/(height**2)

print(f"Your BMI is: {bmi}")


if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You have normal weight")
elif bmi < 30:
    print("You are overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("Critical Obese")

