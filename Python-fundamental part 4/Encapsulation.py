class Bank_account:
    def __init__(self,name,balance):
        self._name=name;
        self.__balance=balance;
        
    def get_amount(self):
        print(self.__balance)
        
    def set_amount(self,bal):
        self.__balance=bal
        
b1=Bank_account("harsh",2000000000);
print(b1._Bank_account__balance)
b1.set_amount(21000000000000000000)
print(b1._name)

b1.get_amount()

#********************************************** hi I am Harsh ___________________..............

#code comment using Ai

# Class definition
class Bank_account:

    # Constructor - called automatically when an object is created
    def __init__(self, name, balance):
        self._name = name          # Protected attribute (can be accessed outside, but by convention shouldn't be)
        self.__balance = balance   # Private attribute (name mangling is applied)

    # Getter method - used to access the private balance
    def get_amount(self):
        print(self.__balance)

    # Setter method - used to update the private balance
    def set_amount(self, bal):
        self.__balance = bal


# Creating an object of the Bank_account class
b1 = Bank_account("harsh", 2000000000)

# Accessing the private variable using Python's name mangling
# Normally, b1.__balance would raise an AttributeError
print(b1._Bank_account__balance)

# Updating the private balance using the setter method
b1.set_amount(21000000000000000000)

# Accessing the protected variable
print(b1._name)

# Accessing the updated private balance using the getter method
b1.get_amount()