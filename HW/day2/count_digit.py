def count_digit(a):
    count=0
    while a>0:
        count=count+1
        a % 10
        
        a=a//10;
    print("====count",count);
        
count_digit(122)