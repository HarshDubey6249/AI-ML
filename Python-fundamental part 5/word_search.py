data=True
line =1
word="solved"
with open("word_search.txt","r") as f:
    while data:
        data=f.readline();
        if(word in data):
            print(f"{word}  find in line {line}");
            break;
        
        line+=1
        print(data)