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
        items = ''
        if len(self.menu) > 0:
            for item in self.menu:
                items+=f"{item.name}/"
        else:
            print("Menu empty")
        return items[:-1]
    
    def get_items_list(self):
        item_list = []
        if len(self.menu) > 0:
            for item in self.menu:
                item_list.append(item.name)
        else:
            print("Menu empty")
        return item_list
    
    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        return None
    
            