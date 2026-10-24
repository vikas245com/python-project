print("--- Mini Contact Book---")
contact = []
while True:
    print("1. Add contact ")
    print("2. view all contact ")
    print("3. Search contact ")
    print("4. Exit ")
    num = input("Please select a number given! ")
    if num == "1":
        name = input ("Enter contact name! ")
        contact_number = int(input ("Enter contact number! "))
        contact_diary = {
            "Name" : name,
            "contact number" : contact_number,
        }
        contact.append(contact_diary)
    elif num == "2":
        if not contact:
            print("contact list empty!")
        else:
            for item in contact:
                print(item)
    elif num == "3":
        if not contact: 
            print("no contact list added")
        else:
            search_name = input("Enter name to search:")
            found = False
            for item in contact:
                if item["Name"] == search_name:
                    print(f"phone number: {item['contact number']}")
                    found = True
                    break
            if not found:
                print("contact not found! ")

    elif num == "4":
        print("program band ho raha hai! ")
        break
    else:
        print("only 1 se 4 tak number hee add kare!")

        