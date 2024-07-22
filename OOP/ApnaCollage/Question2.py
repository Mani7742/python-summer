class Account:
    balance = 0
    Account_No = 1
    def __init__(self, balance, Account_No):
        self.balance = balance
        self.Account_No = Account_No

    def Debit(self, Amount):
        self.balance = self.balance - Amount
        print("Rs.",Amount,"was debited")
        print("Current Balance is Rs.",self.balance)

    def Credit(self, Amount):
        self.balance = self.balance + Amount
        print("Rs.",Amount,"was Credited")
        print("Current Balance is Rs.",self.balance)

    def get_Balance(self):    
        print("Your Balance is Rs.",self.balance)

acc1 = Account(2500,1)
# print(acc1.balance)
# print(acc1.Account_No)
acc1.Debit(1000)
acc1.Credit(1500)
acc1.get_Balance()