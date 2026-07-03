class BankAccount:
    def __init__(self,ac_num,owner_name,balance):
        self.ac_num=ac_num;
        self.owner_name=owner_name;
        self.balance=balance;
        
    def info(self):
        print(f" acc_num = {self.ac_num}  owner_name= {self.owner_name}  balance  is ={self.balance}");
    # Deposit 
    def deposite(self,balance):
        self.balance+=balance;
        
    def withdraw(self,amount):
        if(amount > self.balance):
         print("Insufficient Balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

        
    def cheak_balance(self):
        print(f"Your acc balance is {self.balance}");
        
    
a1= BankAccount(1,"harsh",1000);
a1.info()
a1.deposite(1000); 
a1.info() 
a1.withdraw(10000);  
a1.cheak_balance() 
