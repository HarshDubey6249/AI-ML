students={}

while True:
    print("\n--- MENU ---")
    print("A. Add a student")
    print("B. Update marks")
    print("C. Search for a student")
    print("D. Display all students")
    print("E. Exit")
    
    choice=input("Enter your choice between A-E: ").upper();
    
    if(choice=="A"):
        name=  input("Enter student name:  ");
        mark = int(input("Enter student mark: "))
        
        students[name]=mark
        print("student add successfully in dist");
        
    elif(choice=="B"):
            name = input("Enter student name to update: ")
            if name in students:
                marks = int(input("Enter new marks: "))
                students[name] = marks
                print("Marks updated successfully!")
            else:
                print("Student not found!")
    elif(choice=="C"):
            name = input("Enter student name to update: ")
            if name in students:
                print(f"{name} is ontain mark{students[name]} be happy");
            else:
                print("Student not found!")        
    elif(choice=="D"):
            if students:
                print("--Student Record---")
                
                for name,marks in students.items():
                    print(f"{name}:{marks}")
            else:
                print("No records found.")
    elif choice == 'E':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
        
    



    
