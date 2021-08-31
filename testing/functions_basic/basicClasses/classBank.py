class User:
    def __init__(self, name, initDeposit):
        self.name = name
        self.balance = initDeposit
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawl(self, amount):
        self.balance -= amount
        return self
    def display_user_balance(self):
        print("User: %s\nBalance: $%d\n" %(self.name, self.balance))
        return self
    def transfer_money(self, otherUser, amount, reason):
        self.balance -= amount
        otherUser.balance += amount
        print("Transfer of $%d for %s successful!\nNew Balance: $%d" %(amount, reason, self.balance))
        return self
Nathan = User("Nathan", 50)
Bob = User("Bob", 10)
unknown = User('none', 0)
Nathan.make_deposit(50).make_deposit(30).make_deposit(50).make_withdrawl(100).display_user_balance()
Bob.make_deposit(50).make_deposit(30).make_withdrawl(10).make_withdrawl(70).display_user_balance()
unknown.make_deposit(10000).make_withdrawl(1000).make_withdrawl(40).make_withdrawl(9000).display_user_balance()
#bonus
Nathan.transfer_money(unknown,50,"gas")
