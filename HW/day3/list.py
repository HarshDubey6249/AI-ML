words = ["apple", "banana", "kiwi", "cherry", "mango"]

print("start program for Create a Dictionary that Maps Each Word to Its Length")

dist={}

for i in words:
    length=len(i);
    print(length)
    dist[i]=length
print(dist)