class MoneyMachine:
    def __init__(self, fund=0):
        self.fund = fund
    
    def report(self):
        print(self.fund)