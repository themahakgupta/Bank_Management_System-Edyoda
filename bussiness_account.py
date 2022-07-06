class bussiness_account:
    def __init__(self,cash,total_amount):
        self.total_amount=(total_amount)
        self.cash=cash

    def credit_bussiness(self):
        print(f"The current amount in your account is:{self.cash} INR")
        amount=float(input("Enter the amount you want to deposit:"))
        if amount>0 and amount<=100000:
            self.total_amount=amount+self.cash
            print("Amount credited successfully!!!")
            print(f"The total amount in your account is:{self.total_amount}INR")
            print("Thank You For Choosing SBI")
        else:
            print("Invalid Amount Entered!!!!! Please Login again") 

    def debit_bussiness(self):
        print(f"The current amount in your account is:{self.total_amount}INR")
        amount=float(input("Enter the amount you want to debit:"))
        if amount<=self.total_amount and amount<=50000:
            self.total_amount=self.total_amount-amount
            print("Amount debited successfully!!!!")
            print(f"The total amount in your account is {self.total_amount}INR")
            print("Thank You For Choosing SBI")
        else:
            print("Insufficient Amount!!!!") 

