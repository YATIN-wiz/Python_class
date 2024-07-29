class Bankaccount:
    def __init__(self,account_no,acc_holder,balance = 0):
        self.accno = int(account_no)
        self.accholder = acc_holder
        self.balance = int(balance)

    def deposit(self):
        amount = float(input("Enter the amount to be deposited:"))
        self.balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter the amount to be withdrawn:"))
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insuffient blance")


    def display(self):
        print("Accont NO:", self.accno)
        print("Accont holder:", self.accholder)
        print("Balance:", self.balance)

bank = Bankaccount(input("Enter account no"),input("Enter account holder "))

bank.deposit()
bank.withdraw()
bank.display()
            
            
