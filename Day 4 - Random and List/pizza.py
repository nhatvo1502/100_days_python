print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

price = 0
if size == "S":
    price += 15
    if add_pepperoni == "Y":
        price+=2
    elif extra_cheese=="Y":
        price+=1
    else:
        pass
elif size == "M":
    price += 20
    if add_pepperoni =="Y":
        price+=3
    elif extra_cheese=="Y":
        price+=1
    else:
        pass
elif size == "L":
    price += 25
    if add_pepperoni =="Y":
        price+=3
    elif extra_cheese=="Y":
        price+=1
    else:
        pass


print(price)
# elif size == "L":
#     price += 25
#      if add_pepperoni =="Y":
#         price+=3
#     elif extra_cheese=="Y":
#         price+=1
#     else:
#         pass
# else:
#     pass

# print(price)