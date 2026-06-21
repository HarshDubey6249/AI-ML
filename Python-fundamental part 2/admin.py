admin_name=input("enter your admin name : ");
admin_pass=input("enter you admin password : ");

if(admin_name=="harsh" and admin_pass=="pass"):
    print("you are succesfully entern in system")
else:
    if(admin_name!="harsh" and admin_pass!="pass"):
        print("name and password is wrong");
    elif(admin_name!="harsh"):
        print("your name is wrong")
    else:
         print("your password is wrong")
        