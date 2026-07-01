try:
    x=int(input("enter your number = "));
    ans=10/x;
    
except ZeroDivisionError:
    print("Divivde by 0 is not allowed");
except ValueError:
    print ("Invalid input");
else:
    print(f"ans= {ans}");
