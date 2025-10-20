from menu import MenuItem

class CoffeeMaker:
    def __init__(self, water=300, milk=200, coffee=100, fund=0.0):
        self.resource = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
            "fund": fund
        }
    
    def report(self):
        print(f"Water: {self.resource["water"]}")
        print(f"Milk: {self.resource["milk"]}")
        print(f"Coffee: {self.resource["coffee"]}")
        print(f"Money: {self.resource["money"]}")
    
    def is_resource_sufficient(self, drink):
        isSufficient = False
        if drink.ingredient["water"] < self.resource["water"]:
            if drink.ingredient['milk'] < self.resource["milk"]:
                if drink.ingredient['coffee'] < self.resource["coffee"]:
                    isSufficient =  True
                else:
                    print("Not enough coffee.")
            else:
                print("Not enough milk.")
        else:
            print("Not enough water.")
        return isSufficient
    
    def make_coffee(self, order):
        self.resource["water"]-=order.ingredient["water"]
        self.resource["milk"]-=order.ingredient["milk"]
        self.resource["coffee"]-=order.ingredient["coffee"]
        self.resource["fund"]+=order.ingredient["cost"]