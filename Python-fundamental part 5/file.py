#f=open("sample.txt","r");  #return file obj

#Access ile in data and store in data variable

# data=f.read();
# print(data);
#read the data

# f.close();

#write the data
# f=open("sample.txt","w");
# data=f.write("data is over write using write fun");
# print(data);
# f.close()

# write the data append value 

f=open("sample.txt","a");
data=f.write("I am  harsh Dubey");

f.close()