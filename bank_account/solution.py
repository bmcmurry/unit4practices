class BankAccount:
    defaultnumber = 1

    def __init__(self, name) -> None:
        self.name = name
        self.accountnumber = BankAccount.defaultnumber
        self.balance = 0
        BankAccount.defaultnumber += 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError
        self.balance -= amount

    def getBalance(self):
        return "${:,.2f}".format(self.balance)
