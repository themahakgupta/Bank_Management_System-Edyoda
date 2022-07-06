from current_account import *
from saving_account import *
from bussiness_account import *
class Account:
    def __init__(self,current_obj,saving_obj,bussiness_obj):
        self.current_obj=current_obj
        self.saving_obj=saving_obj
        self.bussiness_obj=bussiness_obj
    def execute(self,choice):
        if choice==1:
            print("*********** Login As Current Account**********")
            self.name=input("Enter your name: ")
            self.account_no=input("Enter your account number:")
            self.passowrd=input("Enter your pin:")
            self.phone_no=(input("Enter your phone number:"))
            self.branch_name=input("Enter your branch name:")
            if len(self.name)!=0 and len(self.account_no)==11 and self.account_no.isdigit() and len(self.passowrd)>=4  and len(self.phone_no)==10 and len(self.branch_name)!=0:
                print("Logged In Successfully To Current Account!!!!")
                print(f"Welcome:{self.name} \nAccount Number:{self.account_no} \nPhone Number:{self.phone_no} \nBranch Name:{self.branch_name} \n")
                choice=1
                while choice!=0:
                    choice=int(input("Enter\n1.Credit Amount\n2.Debit Amount\n0.Exit\n"))
                    if choice==1:
                        print("**********Credit Amount********")
                        self.current_obj.credit_current()
                    elif choice==2:
                        print("**********Debit Amount*********")
                        self.current_obj.debit_current()
                    else:
                        print("Invaild Credentials!!!!!")
            else: 
                print("Invalid input credentials!!!. Please login again")



        elif choice==2 :
            print("************ Login As Saving Account********")
            self.name=input("Enter your name: ")
            self.account_no=input("Enter your account number:")
            self.passowrd=input("Enter your pin:")
            self.phone_no=(input("Enter your phone number:"))
            self.branch_name=input("Enter your branch name:")
            if len(self.name)!=0 and len(self.account_no)==11 and self.account_no.isdigit() and len(self.passowrd)>=4  and len(self.phone_no)==10 and len(self.branch_name)!=0:
                print("Logged In Successfully To Saving Account!!!!")
                print(f"Welcome:{self.name} \nAccount Number:{self.account_no} \nPhone Number:{self.phone_no} \nBranch Name:{self.branch_name} \n")
                choice=1
                while choice!=0:
                    choice=int(input("Enter\n1.Credit Amount\n2.Debit Amount\n0.Exit\n"))
                    if choice==1:
                        print("**********Credit Amount********")
                        self.saving_obj.credit_saving()
                    elif choice==2:
                        print("**********Debit Amount*********")
                        self.saving_obj.debit_saving()
                    else:
                        print("Invaild Credentials!!!!!")
            else:
                print("Invalid input credentials.Please login again!!!!!")

        elif choice==3:
            print("************ Login As Bussiness Account************" )
            self.name=input("Enter your name: ")
            self.account_no=input("Enter your account number:")
            self.passowrd=input("Enter your pin:")
            self.phone_no=(input("Enter your phone number:"))
            self.branch_name=input("Enter your branch name:")
            if len(self.name)!=0 and len(self.account_no)==11 and self.account_no.isdigit() and len(self.passowrd)>=4  and len(self.phone_no)==10 and len(self.branch_name)!=0:
                print("Logged In Successfully To Bussiness Account!!!!")
                print(f"Welcome:{self.name} \nAccount Number:{self.account_no} \nPhone Number:{self.phone_no} \nBranch Name:{self.branch_name} \n")
                choice=1
                while choice!=0:
                    choice=int(input("Enter\n1.Credit Amount\n2.Debit Amount\n0.Exit\n"))
                    if choice==1:
                        print("**********Credit Amount********")
                        self.bussiness_obj.credit_bussiness()
                    elif choice==2:
                        print("**********Debit Amount*********")
                        self.bussiness_obj.debit_bussiness()
                    else:
                        print("Invaild Credentials!!!!!")
            else:
                print("Invalid input credentials. Please login again!!!!!")


        else:
            print("Invaild Account Number or Password")
            print("Thank You For Chosing State Bank Of India. Have A Good Day!!!!!")

if __name__=="__main__":
    print("Welcome To State Bank Of India")
    cash1=int(input("Enter amount:"))
    current_obj=current_account(cash=cash1,total_amount=float)
    saving_obj=saving_account(cash=cash1,total_amount=float)
    bussiness_obj=bussiness_account(cash=cash1,total_amount=float)
    account_obj=Account(current_obj,saving_obj,bussiness_obj)
    choice=1
    while choice !=0:
        
        choice=int(input("Enter \n1. Login as Current Account \n2. Login as Saving Account \n3. Login as Bussiness Account \n0.Exit \n"))
        account_obj.execute(choice=choice)





