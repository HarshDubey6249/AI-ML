class Laptop:
    storage_type="ssd"
    
    def __init__(self,RAM,Storage):
        self.RAM=RAM;
        self.Storage=Storage;
        
    @classmethod
    def get_Storage_type(cls):
            print(f"storage type ={cls.storage_type}")
    def get_info(self):
            print(f"Laptop has {self.RAM} RAM & {self.stroage_type}");
    
    @staticmethod
    def cal_discount(price,discount):
        final_price=price-(discount*price/100);
        print(f"final p[rice= {final_price}");
l1=Laptop("16gb","521gb")


l1.cal_discount(40_000,10);

#below have commented code by Ai

# Define a class named Laptop
class Laptop:

    # Class Variable (shared by all objects)
    storage_type = "ssd"

    # Constructor - runs automatically when an object is created
    def __init__(self, RAM, Storage):
        # Instance Variables (different for each object)
        self.RAM = RAM
        self.Storage = Storage

    # Class Method
    # Used to access or modify class variables
    @classmethod
    def get_Storage_type(cls):
        print(f"Storage Type = {cls.storage_type}")

    # Instance Method
    # Used to access instance variables
    def get_info(self):
        print(f"Laptop has {self.RAM} RAM & {self.storage_type} storage")

    # Static Method
    # Independent of both class and object data
    @staticmethod
    def cal_discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"Final Price = {final_price}")


# Create an object of the Laptop class
l1 = Laptop("16GB", "512GB")

# Call Static Method using object
l1.cal_discount(40_000, 10)

# Call Class Method
l1.get_Storage_type()

# Call Instance Method
l1.get_info()
        