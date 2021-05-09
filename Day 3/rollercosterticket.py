print("Welcome to the rollercosters!:")
height = int(input("What is your height in cm? "))
age = int(input("How old are you? "))

if height >= 120:
    if age >= 18:
        print("Please pay $12.")
    else: 
        print("Please pay $7.")
else:
    print("Too short baby")
