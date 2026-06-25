class Student:
    
    college_name="nirmala memorial foundation college"
    
    
    def __init__(self,name,cgpa):
        self.name=name;
        self.cgpa=cgpa;
        
    
s1=Student("harsh",9.6);
print(s1.name);
print(Student.college_name);

#-----------------------------------
# Code comment by AI

class Student:

    # Class variable (shared by all objects)
    college_name = "nirmala memorial foundation college"

    # Constructor
    def __init__(self, name, cgpa):
        # Instance variables (different for each object)
        self.name = name
        self.cgpa = cgpa


# Creating an object
s1 = Student("harsh", 9.6)

# Accessing instance variable
print(s1.name)

# Accessing class variable
print(Student.college_name)