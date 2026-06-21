info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
]

empty_set=set();

for name, course in info:
    
  #empty_set.add(i[1]);
   if (course=="English"):
        print(name)

#print(empty_set)
    
dist={};  
for name ,cours in info:
    if(dist.get(name)==None):
        dist.update({name:set()})
        dist[name].add(cours);
    else:
        dist[name].add(cours);
        
print(dist)
    
    