
class Bank(object):

    def __init__(self, name):
        self.name = name
        self.transactions = {}
        self.i = 0

    def __str__(self):
        return self.name + ': ' + str(self.view_balance())

    def view_balance(self):
        self.balance = sum(self.transactions.values())
        return self.balance

    def deposit(self, amount):
        self.i += 1
        self.transactions[self.i] = amount

    def withdrawal(self, amount):
        if amount <= self.view_balance():
            self.i += 1
            self.transactions[self.i] = -(amount)

    def view_transactions(self):
        return self.transactions

# Things to add:
#
# day and night cycles
# save game
