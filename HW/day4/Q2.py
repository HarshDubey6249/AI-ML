class Book:
    
    def __init__(self,title,author,list_reviews):
        self.title=title;
        self.author=author;
        self.list_reviews=list_reviews
        
    def info(self):
        print(f"Book Title = {self.title}");
        print(f"book Author= {self.author}");
        print(f"list of reviwes {self.list_reviews}");
        
    def count_reviews(self):
        count=len(self.list_reviews);
        print(f"Total Reviews is {count}");
        
    def add_reviews(self,reviews):
        self.list_reviews.append(reviews);
        print("Reviews add successfully");
        
    def show_reviews(self):
        print(f"reviews is ={self.list_reviews}");
        
    
        
        
b1=Book("M.I.A","author",["Very nice ","Excellent","Amazing"]);

b1.show_reviews()
b1.add_reviews("harsh");
b1.count_reviews();
b1.show_reviews()