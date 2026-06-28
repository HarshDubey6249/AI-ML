# Multiple level

# class Employee:
#     start_time="10am"
#     end_time="6pm"
    
   

# class Adminstracton(Employee):
#     def __init__(self,role):
#         self.role=role;
        
# class Accountant(Adminstracton):
#     def __init__(self,salary, role):
#         super().__init__(role)
#         self.salary=salary;
        
# acc1 =Accountant(2500000,"IT");

# print(acc1.salary);
# print(acc1.role)
    
        
#MUltiple level



class Teacher:
    def __init__(self,salary):
        self.salary=salary;
        
class Student:
    def __init__(self,gpa):
        self.gpa=gpa;
        
class TA(Teacher,Student):
    def __init__(self, salary,gpa,subject):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.subject=subject
        
        
ta1=TA(150000,9.5,"math");

print(ta1.subject);
print(ta1.gpa)
print(ta1.salary)

#********************************************** hi I am Harsh ___________________..............

#code comment using Ai

# ==========================================================
#               MULTILEVEL INHERITANCE
# ==========================================================

# Parent Class
# class Employee:

#     # Class variables shared by all child classes
#     start_time = "10am"
#     end_time = "6pm"


# Child Class
# Inherits from Employee
# class Administration(Employee):

#     # Constructor of Administration
#     def __init__(self, role):

#         # Creates an instance variable 'role'
#         self.role = role


# Grandchild Class
# Inherits from Administration
# class Accountant(Administration):

#     # Constructor of Accountant
#     def __init__(self, salary, role):

#         # Calls Administration constructor
#         # This initializes self.role
#         super().__init__(role)

#         # Creates instance variable salary
#         self.salary = salary


# Creating Accountant object
# acc1 = Accountant(2500000, "IT")


# Printing Accountant details
# print(acc1.salary)      # 2500000
# print(acc1.role)        # IT



# ==========================================================
#               MULTIPLE INHERITANCE
# ==========================================================

# First Parent Class
class Teacher:

    # Constructor
    def __init__(self, salary):

        # Instance variable
        self.salary = salary


# Second Parent Class
class Student:

    # Constructor
    def __init__(self, gpa):

        # Instance variable
        self.gpa = gpa


# Child Class
# Inherits from both Teacher and Student
class TA(Teacher, Student):

    # Constructor
    def __init__(self, salary, gpa, subject):

        # Calls Teacher constructor using super()
        # Creates:
        # self.salary
        super().__init__(salary)

        # Calls Student constructor explicitly
        # Creates:
        # self.gpa
        Student.__init__(self, gpa)

        # Creates subject variable
        self.subject = subject


# Creating TA object
ta1 = TA(150000, 9.5, "math")


# Printing instance variables
print(ta1.subject)     # math
print(ta1.gpa)         # 9.5
print(ta1.salary)      # 150000

