class BankAccount:
    def __init__(self,Name,Balance):
        self.name=Name
        self.balance=Balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Amount Deposited :",amount)

    def withdrawal(self,amount):
        if self.balance>=amount:
            self.balance=self.balance-amount
            print("Withdraw Successfully:",amount)

        else:
            print("Insufficient balance")

    def display(self):
        print("Name:",self.name)
        print("Balance:",self.balance)




# account=BankAccount("Haris",10000)
# account.deposit(5000)
# account.withdrawal(2500)
# account.display()

Name=(input("Enter the Name :"))
Balance=float(input("Enter your initial balance:"))

account=BankAccount(Name,Balance)

account_deposit=float(input("Enter your deposit amount:"))
account.deposit(account_deposit)

account_withdrawal=float(input("Enter your withdrawal amount:"))
account.withdrawal(account_withdrawal)

account.display()