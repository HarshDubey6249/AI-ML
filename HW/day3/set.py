list1 = [5,2,3,4,5,6]
# list2 = [5,6,7,8]

# if set(list1).isdisjoint(set(list2)):
#     print("No common elements")
# else:
#     print("Common elements exist")

duplicate=set();

for i in  list1:
    if list1.count(i)>1:
        duplicate.add(i);
print(duplicate)