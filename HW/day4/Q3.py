class Student:
    def __init__(self,name,roll_num):
        self.set_name(name);
        self.set_roll_num(roll_num);
        # self.set_mum_mark(num_mark);
        
    def set_name(self,name):
        if name.strip()=="":
           print("Name cannot be empty!")
        else:
            self._set_name = name
            
    def set_roll_num(self,rollNum):
        self._set_roll_num = rollNum
     
            
            
            
    def get_name(self):
        print(self._set_name);
        
    def get_roll(self):
        print(self._set_roll_num);
        

s1 = Student("Harsh",34)

s1.get_name();
s1.set_name("Aryan")
s1.get_name();
s1.get_roll()
s1.set_roll_num(45);
s1.get_roll()

        