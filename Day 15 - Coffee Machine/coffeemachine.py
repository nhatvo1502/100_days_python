# Resources


RESOURCE = {
   "WATER": 0,
   "MILK": 0,
   "COFFEE": 0,
   "MONEY": 0.0
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

def turn_off():
   '''Turn off the machine for maintenance'''
   return 0

def print_report():
   print(f"Water :{RESOURCE["WATER"]}")
   print(f"Milk: {RESOURCE["MILK"]}")
   print(f"Coffee: {RESOURCE["COFFEE"]}")
   print(f"Money: {RESOURCE["MONEY"]}")

def check_resource_sufficient(order):
   '''Check if there are enough resources to make the order'''
   '''return True/False'''
   isSufficient = False
   if order['drink']["water"] > RESOURCE["WATER"] and order['drink']["milk"] > RESOURCE["MILK"] and order['drink']["coffee"] > RESOURCE["COFFEE"]:
      isSufficient = True

   return isSufficient

def process_coins(order):
   '''calculate values of inserted coins'''
   '''return values'''
   coin_value = order[0]['quarters']*0.25 + order[0]['dimes']*0.10 + order[0]['nickles']*0.05 + coins['pennies']*0.1
   order.updated({"money": coin_value})

def check_transaction(order):
   '''check if inserted coins is sufficient to purchase the drink'''
   '''return True or False'''
   isSuccessful = False
   inserted_coins = process_coins(order)
   change = inserted_coins - MENU[order['drink']]['price']
   if change >= 0:
      isSuccessful = True
      if change > 0:
         refund(change)
   else:
      print("Sorry that's not enough money. Money refunded")
      refund(inserted_coins)
   return isSuccessful

def refund(money):
   '''print refund money'''
   '''return nothing'''
   print(f"Refunding: {money}")

def restocking():
   isRestocking = True
   while isRestocking:
      choice = input("Which resource do you want to restock? (water/mill/coffee/money) ")
      value = None
      if choice == 'money':
         value = float(input('Please input the amount: '))
      else:
         value = input('Please input the amount: ')
      RESOURCE[choice]+=value
      choice = input("Are you done? (y/n)")
      if choice == y:
         isRestocking = False

def make_coffee(order):
   RESOURCE["WATER"]-=MENU[order['drink']['water']]
   RESOURCE["COFFEE"]-=MENU[order['drink']['coffee']]
   RESOURCE["MILK"]-=MENU[order['drink']['milk']]
   RESOURCE["MONEY"]+=MENU[order['cois']]