# My code
class Student:
    def __init__(self,name,subject):
        self.name=name;
        self.subject=subject;
    
    def get_info(self):
         return self.name;
        
        
        
        
        
s1= Student("harsh","math")
s2= Student("trisha","math")

print(s1.get_info());
print(s1.subject)
print(s2.name);
print(s2.subject)




#--------------------------------------------

# Code comment by AI

# Define a class named Student
class Student:

    # Constructor: runs automatically when an object is created
    def __init__(self, name, subject):
        self.name = name        # Store the student's name
        self.subject = subject  # Store the student's subject

    # Method to return the student's name
    def get_info(self):
        return self.name


# Create the first Student object
s1 = Student("harsh", "math")

# Create the second Student object
s2 = Student("trisha", "math")

# Call the get_info() method for s1
print(s1.get_info())   # Output: harsh

# Access the subject attribute of s1
print(s1.subject)      # Output: math

# Access the name attribute of s2
print(s2.name)         # Output: trisha

# Access the subject attribute of s2
print(s2.subject)      # Output: maths