class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredient = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("espresso", 50, 0, 18, 1.50),
            MenuItem("latte", 200, 150, 24, 2.50),
            MenuItem("cappuccino", 250, 100, 24, 3.00)
        ]

    def update(self, items):
        for item in items:
            self.menu.append(item)
    
    def get_items(self):
        if len(self.menu) > 0:
            items = ''
            for item in self.menu:
                items+=f"{item.name}/"
            return items[:-1]
        else:
            print("Menu empty")
    
    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        return None
    
            