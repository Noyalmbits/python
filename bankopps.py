class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)
        print("Current balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
            print("Current balance:", self.balance)
        else:
            print("Insufficient balance")

b1 = BankAccount(101, "Anu", "Savings", 5000)
print("Account Number:", b1.acc_no)
print("Name:", b1.name)
print("Account Type:", b1.acc_type)
print("Balance:", b1.balance)
b1.deposit(2000)
b1.withdraw(1000)

