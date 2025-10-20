from coffee_maker import CoffeeMaker
import money_machine
from menu import MenuItem, Menu

menu = Menu()
print(menu.get_items())
print(menu.find_drink('latte'))

coffee_maker = CoffeeMaker()
coffee_maker.report()
print(coffee_maker.is_resource_sufficient(menu.find_drink('latte')))
