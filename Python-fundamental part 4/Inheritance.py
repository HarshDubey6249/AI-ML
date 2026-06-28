class Employee:
    start_time="10am"
    end_time="6pm"
    
    def change_time(self, end_time):
        self.end_time=end_time;
        
    
class Teacher(Employee):
    def __init__(self,subject):
        self.subject=subject;
        

t1=Teacher("math");

print(t1.subject);
print(t1.start_time);
print(t1.end_time);

print("--------------------------------")

t1.change_time("5pm");
print(t1.end_time);

#********************************************** hi I am Harsh ___________________..............

#code comment using Ai


# Parent Class
class Employee:
    
    # Class variables (shared by all Employee and Teacher objects)
    start_time = "10am"
    end_time = "6pm"
    
    # Method to change end time for a specific object
    def change_time(self, end_time):
        self.end_time = end_time   # Creates/updates instance variable


# Child Class (inherits from Employee)
class Teacher(Employee):
    
    # Constructor
    def __init__(self, subject):
        self.subject = subject


# Creating an object of Teacher
t1 = Teacher("math")

# Printing Teacher's subject
print(t1.subject)

# Accessing inherited class variable
print(t1.start_time)

# Accessing inherited class variable
print(t1.end_time)

print("--------------------------------")

# Changing end time only for object t1
t1.change_time("5pm")

# Now instance variable is printed instead of class variable
print(t1.end_time)

# *******************************************************