bill = 1
while bill > 0:
    print("Welcome to the tip calculator.")
    bill = float(input("What was the total bill? "))
    tip = int(input ("What percentage tip would you like to give? 10, 12, or 15? "))
    people = int(input ("How many people to split the bill? "))

    bill_per_person = bill * (tip/100 + 1) / people
    bill_per_person  = round(bill_per_person , 2)
    final_amount = "{:.2f}".format(bill_per_person)
    print(f"Each person should pay: {final_amount}")