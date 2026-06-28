class Employee:
    start_time="10am"
    end_time="6pm"
    
   

class Adminstracton(Employee):
    def __init__(self,role):
        self.role=role;
        
class Accountant(Adminstracton):
    def __init__(self,salary, role):
        super().__init__(role)
        self.salary=salary;
        
acc1 =Accountant(2500000,"IT");

print(acc1.salary);
print(acc1.role)
    
        
    

        

