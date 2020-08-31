
# Program for managing activities in library

Books = ["Mrutyunjay", "Shriman Yogi", "Dasbodh", "Dnyaneshwari"]

user_ids = {"Ram":"999"}

def Create_new_account():
    print("Want to Create account? If yes type y otherwise n")
    new_user_account_permission = input("y or n? : ")
    if new_user_account_permission == "y":
        print("Your username is nothing but your name.")
        new_user_name = input("Enter your name : ")
        print("Now set your password")
        new_user_pass = input("Enter password you want to set : ")
        new_user_id = f"{new_user_name} : {new_user_pass}"
        user_ids[new_user_name] = new_user_pass
        print(user_ids)
    else:
        print("Sorry to see you leaving!")
        exit()

def Regular_user_activity():
    print("What do you want to do?\nBorrow a book, Submit a book, Gift a book.\nType Borrow, Submit or Gift")
    regular_user_activity_type = input("Enter activity to do : ")
    if regular_user_activity_type.capitalize() == "Borrow":
        print(Books)
        regular_user_book_borrow_name = input("Enter name of book you want to borrow: ")
        if regular_user_book_borrow_name in Books:
            Books.remove(regular_user_book_borrow_name)
            print(Books)
        else:
            print("We don't have such book OR Invalid input")
    elif regular_user_activity_type.capitalize() == "Submit":
        print(Books)
        regular_user_book_submit_name = input("Enter name of book you want to submit : ")
        Books.append(regular_user_book_submit_name)
        print(Books)
    elif regular_user_activity_type == "Gift":
        print(Books)
        regular_user_book_gift_name = input("Enter name of book you want to gift : ")
        Books.append(regular_user_book_gift_name)
        print(Books)

def Check_regular_user():
    user_name_input = input("What is your name? : ")
    for key, value in user_ids.items():
        if user_name_input == key.capitalize():
            user_pass = input("Enter your password : ")
            if user_pass == value:
                # print("What do you want to do?")
                Regular_user_activity()
            else:
                print("Sorry, wrong password")
        else:
            print("You don't have account.")

def Guest_activity():
    print("What do you want to do?\nYou can See the list of books, Gift a book or create an account.\nType Book_list, Gift.")
    guest_activity_type = input("Enter what do you want to do? : ")
    if guest_activity_type == "Book_list":
        print(Books)
    elif guest_activity_type == "Gift":
        print(Books)
        print("Please enter name of the book you want to gift the libraray.")
        guest_book_gift_name = input("Enter name of the book you want to gift : ")
        Books.append(guest_book_gift_name)
        print(Books)
    else:
        pass

print("Welcome to Our Library !\nHow do you want to continue - Guest, Regular_user, New_user")
user_type = input("Guest, Regular_user, New_user : ")
if user_type.capitalize() == "Guest":
    Guest_activity()
    Create_new_account()
elif user_type.capitalize() == "New_user":
    Create_new_account()
elif user_type.capitalize() == "Regular_user":
    Check_regular_user()
else:
    print("Wrong Input!")
