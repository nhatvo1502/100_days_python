year = int(input("Enter a year: "))

message_1 = f"{year} is leap year"
message_2 = f"{year} is not leap year"
print(year%4)

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(message_1)
        else:
            print(message_2)
    else:
        print(message_1)
else:
    print(message_2)
    