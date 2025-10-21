# Resources
logo = r'''
 ____ ____  _____ _____ _____ _____                           
/   _Y  _ \/    //    //  __//  __/                           
|  / | / \||  __\|  __\|  \  |  \                             
|  \_| \_/|| |   | |   |  /_ |  /_                            
\____|____/\_/   \_/   \____\\____\                           
                                                              
                       _      ____  ____ _     _  _      _____
                      / \__/|/  _ \/   _Y \ /|/ \/ \  /|/  __/
                      | |\/||| / \||  / | |_||| || |\ |||  \  
                      | |  ||| |-|||  \_| | ||| || | \|||  /_ 
                      \_/  \|\_/ \|\____|_/ \|\_/\_/  \|\____\
'''
RESOURCE = {
   "WATER": 300,
   "MILK": 200,
   "COFFEE": 300,
   "MONEY": 1.0
}

MENU = {
   "espresso" : {
      "water": 50,
      "coffee": 18,
      "milk": 0,
      "price": 1.50
   },
   "latte": {
      "water": 200,
      "coffee": 24,
      "milk": 150,
      "price": 2.50
   },
   "cappuccino": {
      "water": 250,
      "coffee": 24,
      "milk": 100,
      "price": 3.00
   }
}

order = {
   "drink": "",
   "pay": {
      "quarters": 0,
      "nickles": 0,
      "dimes": 0,
      "pennies": 0
   },
   "money": 0
}

def turn_off():
   '''Turn off the machine for maintenance'''
   return 0

def print_report():
   print(f"Water: {RESOURCE["WATER"]}ml")
   print(f"Milk: {RESOURCE["MILK"]}ml")
   print(f"Coffee: {RESOURCE["COFFEE"]}g")
   print(f"Money: ${RESOURCE["MONEY"]}")
   
def print_menu():
   print("MENU")
   for i in MENU:
      print(f"{i} {MENU[i]['price']}")

def check_resource_sufficient(order):
   '''Check if there are enough resources to make the order'''
   '''return True/False'''
   drink = order["drink"]
   isSufficient = False
   if MENU[drink]["water"] < RESOURCE["WATER"]:
      if MENU[drink]["milk"] < RESOURCE["MILK"]: 
         if MENU[drink]["coffee"] < RESOURCE["COFFEE"]:
            isSufficient = True
         else:
            print("Sorry there is not enough coffee.")
      else:
         print("Sorry there is not enough milk.")
   else:
      print("Sorry there is not enough water.")

   return isSufficient

def process_coins(order):
   '''calculate values of inserted coins'''
   '''return values'''
   coin_value = order["pay"]['quarters']*0.25 + order["pay"]['dimes']*0.10 + order["pay"]['nickles']*0.05 + order["pay"]['pennies']*0.01
   order.update({"money": round(coin_value, 2)})

def check_transaction(order):
   '''check if inserted coins is sufficient to purchase the drink'''
   '''return True or False'''
   isSufficient = False
   process_coins(order)
   change = order["money"] - MENU[order['drink']]['price']
   if change >= 0:
      isSufficient = True
      if change > 0:
         refund(change)
         order.update({"money": MENU[order['drink']]['price']})
   else:
      print("Sorry that's not enough money. Money refunded")
      refund(order["money"])
   return isSufficient

def refund(money):
   '''print refund money'''
   '''return nothing'''
   print(f"Refunding: ${money:.2f}")

def restock():
   isRestocking = True
   while isRestocking:
      print_report()
      choice = input("Which resource do you want to restock? (water/milk/coffee/money/done) ")
      value = None
      if choice == 'money':
         value = float(input('Please input the amount: '))
      elif choice.upper() in RESOURCE:
         value = int(input('Please input the amount: '))
         RESOURCE[choice.upper()]+=value
      elif choice == "done":
         isRestocking = False
      else:
         print(f"There is no {choice} in resource")

def make_coffee(order):
   RESOURCE["WATER"]-=MENU[order['drink']]['water']
   RESOURCE["COFFEE"]-=MENU[order['drink']]['coffee']
   RESOURCE["MILK"]-=MENU[order['drink']]['milk']
   RESOURCE["MONEY"]+=order['money']
   print(f"Here is your {order["drink"]}. Enjoy ☕!")

def coffee_machine():
   # prompt user to select a drink
   print(logo)
   making_drink = True
   while making_drink:
      drink_selection = input("What would you like? (espresso/latte/cappucino): ")
      if drink_selection == "report":
         print_report()
      elif drink_selection == "turnoff":
         print("Turning off")
         making_drink = False
         return
      elif drink_selection == "menu":
         print_menu()
      elif drink_selection == "restock":
         restock()
      elif drink_selection in MENU:
         this_order = order
         this_order["drink"] = drink_selection

         # check resource if the machine can make this drink
         instock = check_resource_sufficient(this_order)
         # check funds
         if instock == True:
            # insert coins
            print("Please insert coins.")
            this_order["pay"]["quarters"] = int(input("How many quarters?: "))
            this_order["pay"]["dimes"] = int(input("How many dimes?: "))
            this_order["pay"]["nickles"] = int(input("How many nickles?: "))
            this_order["pay"]["pennies"] = float(input("How many pennies?: "))
            transaction = check_transaction(this_order)
            if transaction == True:
               make_coffee(this_order)
      else:
         print("Wrong drink selection. Please try again.")

coffee_machine()