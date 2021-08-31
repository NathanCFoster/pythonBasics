class User:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
    def make_deposit(self, amount, typeof):
        self.accounts[typeof].deposit(amount)
        return self
    def make_withdrawl(self, amount, typeof):
        self.accounts[typeof].withdraw(amount)
        return self
    def display_user_balance(self, typeof):
        print("User: %s\nAccount: %s\nBalance: $%d\n" %(self.name, typeof,self.accounts[typeof].balance))
        return self
    def transfer_money(self, otherUser, amount, reason, typeof):
        self.typeof.account.withdraw -= amount
        otherUser.balance += amount
        print("Transfer of $%d for %s successful!\nNew Balance: $%d" %(amount, reason, self.typeof.account.balance))
        return self
    def interest(self, time, typeof):
        self.accounts[typeof].yieldInterest(time)
        return self
    def makeAcc(self,intRate, balance, typeof):
        self.accounts[typeof] = BankAccount(self.name, intRate, balance)
        return self


class BankAccount(User):
    all_accounts = []
    def __init__(self, user, intRate, balance):
        self.name = user
        self.intRate = intRate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def yieldInterest(self, time):
        for x in range(0, time):
            self.balance *= (self.intRate / 100 + 1)
            self.balance = round(self.balance, 2)
    @classmethod
    def allAccInfo(cls):
        for account in cls.all_accounts:
            print(f"Balance: {account.balance}\nInterest Rate: {account.intRate}%\n")
Nathan = User("Nathan").makeAcc(3,50,"savings").makeAcc(1, 100, "checking").make_deposit(1000,"savings").interest(2, "savings").display_user_balance("checking").display_user_balance("savings")