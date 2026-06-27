class Product:
    
    count=0;
    
    def __init__(self,name,price):
        self.name=name;
        self.price=price;
        Product.count+=1;
        
    def get_info(self):
        print(f" the product = {self.name} is cost={self.price}");
        
    @classmethod
    def get_count(cls):
            print(f"count is: {cls.count}");
            
    @staticmethod
    def get_dis(price,dis):
        print(f"amouunt is {price} after {dis} .final price is { price - (dis * price / 100)}")
        
        
p1 =Product("tv",3453);
p2 =Product("phone",3453);

p3 =Product("ac",3453);

p4 =Product("light",3453);


p1.get_info()
p2.get_info()

p3.get_info()
p4.get_info()



Product.get_count()
print("-------------------")
p1.get_dis(100,30)

print("Thank you visit again")

