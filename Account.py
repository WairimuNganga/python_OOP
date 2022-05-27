#Add these methods to class Account - deposit, withdraw. 
#Create two instances of account and verify they work as expected.
class Account:
    def __init__(self,acc_name,acc_balance,acc_pin,acc_type):
        self.acc_name=acc_name
        self.acc_balance = acc_balance
        self.acc_pin = acc_pin
        self.acc_type = acc_type
    def deposit(self,amount):
        self.amount = amount
        self.acc_balance+=self.amount
        return f"Confirmed {self.acc_name}.You have deposited Kshs.{self.amount}.Your new balance is Kshs.{self.acc_balance}"
    def withdraw(self,amount):
        self.acc_balance-=amount
        return f"Confirmed {self.acc_name}.You have withdrawn Kshs.{self.amount}.Your new balance is Kshs.{self.acc_balance}"

wairimu_nganga = Account("Wairimu Nganga",5000,2000,"Fixed Account")
print(wairimu_nganga .deposit(300))
print(wairimu_nganga .withdraw(500))
shamim_gard = Account("Shamim Gard",1000,1440,"Savings Account")
print(shamim_gard.deposit(100))
print(shamim_gard.withdraw(200))
