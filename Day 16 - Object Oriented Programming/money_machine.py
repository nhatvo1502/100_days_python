class MoneyMachine:

    COIN_VALUES = {
        "quarters": 0.25,
        "nickles": 0.05,
        "dimes": 0.10,
        "pennies": 0.01
    }

    def __init__(self, fund=0.0):
        self.fund = fund
        self.money_received = 0.0
    
    def report(self):
        print(f"Money: ${self.fund}")

    def process_coins(self):
        print("Please insert coin: ")
        for coin in self.COIN_VALUES:
            self.money_received+= int(input(f"How many {coin}?: "))
        print(f"Total insert: ${self.money_received}")
        return self.money_received

    def make_payment(self, cost):
        self.process_coins()
        print(f"Drink price: ${cost}")
        if self.money_received >= cost:
            change = self.money_received - cost
            if self.money_received > cost:
                print(f"Refund ${round(change, 2)}")
            self.fund+=cost
            return True
        else:
            print(f"Insufficient fund. Refund {self.money_received}")
            return False