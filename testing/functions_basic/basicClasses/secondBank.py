
class BankAccount:
    all_accounts = []
    def __init__(self, name, intRate, balance):
        self.name = name
        self.intRate = intRate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"User: {self.name}\nBalance: {self.balance}\nInterest Rate: {self.intRate}%\n")
        return self
    def yieldInterest(self, time):
        for x in range(0, time):
            self.balance *= (self.intRate / 100 + 1)
            self.balance = round(self.balance, 2)
        return self
    @classmethod
    def allAccInfo(cls):
        for account in cls.all_accounts:
            print(f"User: {account.name}\nBalance: {account.balance}\nInterest Rate: {account.intRate}%\n")
Nathan = BankAccount("Nathan", 5, 50).deposit(50).deposit(50).deposit(50).withdraw(80).yieldInterest(3).display_account_info()
John = BankAccount("John", 8, 25).deposit(30).deposit(50).withdraw(60).withdraw(10).withdraw(1).withdraw(1).yieldInterest(5).display_account_info()
BankAccount.allAccInfo()