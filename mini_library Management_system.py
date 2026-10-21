print("--- Mini Librarary Book Manager---")
books_store = []
while True:
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book ")
    print("4. Delete Book")
    print("5. Exit")
    num = input("please select given number! ")
    if num == "1":
        book = input("Enter your book name! ").strip()
        auther = input("Enter your book auther! ").strip()
        book_details = {
            "book" : book,
            "auther" : auther
        }
        books_store.append(book_details)
    if num == "2":
        if not books_store:
            print("book store is empty!")
        else:
            for item in books_store:
                print(item)
    elif num == "3":
        if not books_store:
            print("no books added")
        else:
            search_name = input("Enter your book name! ").strip()
            found = False
            for item in books_store:
                if item["book"] == search_name:
                    print(f"book found -> book: {item['book']}, author: {item['auther']}")
                    found = True
                    break
            if not found:
                print("your book not found")
    elif num == "4":
        if not books_store:
            print("book store is empty, nothing to delete! ")
        else:
            book_to_remove = input("Enter the name of book which do you want to delete! ").strip()
            found = False
            for item in books_store:
                if item["book"] == book_to_remove:
                    books_store.remove(item)
                    print("book deleted successfully!")
                    found = True
                    break
            if not found:
                print("This book is not added in your your list! ")
    elif num == "5":
        print("program band ho raha hai! ")
        break
    else:
        print("only 1 se 5 tak hee number add kare!")
