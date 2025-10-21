from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import MenuItem, Menu
import logo

def main():
   menu = Menu()
   coffee_maker = CoffeeMaker()
   transaction = MoneyMachine()
   print(logo.logo_menu)

   machine_turn_on = True
   while machine_turn_on:
      choice = input("What would you like? (espresso/latte/cappuccino/done) ")
      if choice == "off":
         '''Turn off the machine'''
         return
      
      elif choice == "report":
         '''Print coffee machine resources'''
         print(logo.logo_menu)
         coffee_maker.report()
         transaction.report()

      elif choice in menu.get_items_list():
         '''Selected drinks in the menu'''
         drink = menu.find_drink(choice)
         # check resources sufficient
         resource_is_sufficient = coffee_maker.is_resource_sufficient(drink)
         # process coins + check transaction succesfull
         if resource_is_sufficient == True:
            transaction_succeed = transaction.make_payment(drink.cost)
            if transaction_succeed == True:
               # make coffee
               coffee_maker.make_coffee(drink)
               print(f"Enjoy your {drink.name} ☕")
         
         correct_input = False
         while not correct_input:
            choice = input("Do you want to try again? (y/n) ")
            if choice == 'y':
               correct_input = True
            elif choice == 'n':
               correct_input = True
               machine_turn_on = False
            else:
               print('Wrong input. Please enter y/n')

      elif choice == "done":
         machine_turn_on = False
      else:
         print("Wrong input. Please try again..")

main()