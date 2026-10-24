class Book:
    def __init__ (self, title, auther, copies):
        self.title = title
        self.auther = auther
        self.copies = copies

    def library(self):
        print(f"book title: {self.title}")
        print(f"book auther: {self.auther}")
        print(f"book copies: {self.copies}")
        print("="*30)
    def update_copies(self, new_copies):
        borrow_copies = self.copies - new_copies
        self.copies = borrow_copies
        print(f"copies bacchi hai: {self.copies}")
        print("="*30)
book1 = Book("love story" ,"vikas", 20)
book2 = Book("crime story" , "priya" ,30)
print("--- pahli book ki details ---")
book1.library()
print("--- dusri book ki details ---")
book2.library() 
print("--- borrow hui ki baad bacchi copies ---")
book2.update_copies(10)
print("--- updated detials ---")
book2.library()




