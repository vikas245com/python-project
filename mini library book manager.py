print("--- Mini Library Book Manager---")
books_store = []
while True:
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Exit ")
    num = input("please select given number!")
    if num == "1":
        book = input("Enter your book name! ").strip()
        auther = input("Enter your book auther! ").strip()
        book_details = {
            "book" : book,
            "auther" : auther
        }
        books_store.append(book_details)
    elif num == "2":
        if not books_store:
            print("book store is emptt!")
        else:
            for item in books_store:
                print(item)
    elif num == "3":
        if not books_store:
            print("no books added")
        else:
            search_name = input("Enter your book name!")
            found = False
            for item in books_store:
                if item["book"] == search_name:
                    print(f"book: {item['book']}")
                    print(f"auther: {item['auther']}")
                    found = True
                    break
            if not found:
                print("your book not found")
    elif num == "4":
        print("program band ho raha hai! ")
        break
    else: 
        print("only 1 se 4 tak hee number add kare!")
