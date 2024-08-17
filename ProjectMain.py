class Book:
    def __init__(self, title, author, genre, isbn):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__isbn = isbn
        self.__is_lendable = True

    def get_title(self):
        return self.__title

    def is_lendable(self):
        return self.__is_lendable

    def set_is_lendable(self, status):
        self.__is_lendable = status

    def display_info(self):
        lending_status = "Lendable" if self.__is_lendable else "not_lendable"
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Genre: {self.__genre}")
        print(f"Publication Date: {self.__isbn}")
        print(f"Status: {lending_status}")


class User:
    def __init__(self, name, phone_num, lib_id):
        self.__name = name
        self.__phone_num = phone_num 
        self.__lib_id = lib_id
        self.__lended_books = []
    
    def get_name(self):
        return self.__name
    def get_phone_number(self):
        return self.__phone_num
    def get_lib_id(self):
        return self.__lib_id

    def lend_book(self, book_title):
        self.__books.append({"title": book_title})

    def return_book(self, book_title):
        for book in self.__lended_books:
            if book["title"] == book_title:
                self.__lended_books.remove(book)
                return

    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Phone Number: {self.__phone_num}")
        print(f"Library ID: {self.__lib_id}")
        print("Books that have been lended to you:")


class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Biography: {self.__biography}")


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.lent_books = []

    def main(self): 
        while True: 
            print("Welcome to the Library! Main menu, please select and option")
            print("1. Book Operations ")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Quit")
            choice = input("Please enter a number: ")
            if choice == "1":   
                self.book_operations()    
            elif choice == "2":
                self.user_operations()      
            elif choice == "3":
                self.author_operations() 
            elif choice == "4":
                quit() 
            else:
                print("Invalid selection, please try again")

    def book_operations(self):
        while True:
            print("Book Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")
            ans = input("Enter your choice: ")

            if ans == '1':
                self.add_book()
            elif ans == '2':
                self.borrow_book()
            elif ans == '3':
                self.return_book()
            elif ans == '4':
                self.search_book()
            elif ans == '5':
                self.display_all_books()
            elif ans == '6':
                break
            else:
                print("Invalid entry, please try again.")

    def add_book(self):
        title = input("Enter title of book: ")
        author = input("Enter author of book: ")
        genre = input("Enter genre of book: ")
        isbn = input("Enter isbn number for book: ")
        new_book = Book(title, author, genre, isbn)
        self.books.append(new_book)
        print("Book added successfully.")

    def borrow_book(self):
        title = input("Enter the title of the book to be lent: ")
        for book in self.books:
            if book.get_title() == title and book.is_lendable():
                book.set_is_lendable(False)
                user_id = input("Enter your user ID: ")
                user = self.find_user(user_id)
                if user:
                    user.lend_book(title)
                    print(f"You have been lended '{title}'.")
                return
        print("Book not lendable or not found.")

    def return_book(self):
        title = input("Enter the title of the book to return: ")
        for book in self.books:
            if book.get_title() == title and not book.is_lendable():
                book.is_lendable(True)
                user_id = input("Enter your user ID: ")
                user = self.find_user(user_id)
                if user:
                    user.return_book(title)
                    print(f"You have returned '{title}'.")
                    
                return
        print("Book not found.")

    def search_book(self):
        title = input("What is the title of the book?: ")
        for book in self.books:
            if book.get_title() == title:
                book.display_info()
                return
        print("Book not found.")

    def display_all_books(self):
        if not self.books:
            print("No books available.")
        for book in self.books:
            book.display_info()

    def user_operations(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.view_user_details()
            elif choice == '3':
                self.display_all_users()
            elif choice == '4':
                break
            else:
                print("Invalid entry, please try again.")

    def add_user(self):
        name = input("Enter user name: ")
        lib_id = input("Enter user library ID: ")
        phone_num = input("Enter user phone number: ")
        new_user = User(name, phone_num, lib_id)
        self.users.append(new_user)
        print("User added successfully.")

    def view_user_details(self):
        lib_id = input("Enter user library ID: ")
        for user in self.users:
            if user.get_lib_id() == lib_id:
                user.display_info()
                return
        print("User not found.")

    def display_all_users(self):
        if not self.users:
            print("No users available.")
        for user in self.users:
            user.display_info()

    def find_user(self, lib_id):
        for user in self.users:
            if user.get_lib_id() == lib_id:
                return user
        print("User not found.")
        return None

    def author_operations(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_author()
            elif choice == '2':
                self.view_author_details()
            elif choice == '3':
                self.display_all_authors()
            elif choice == '4':
                break
            else:
                print("Invalid entry, please try again.")

    def add_author(self):
        name = input("Enter author name: ")
        biography = input("Enter author biography: ")
        new_author = Author(name, biography)
        self.authors.append(new_author)
        print("Author added successfully.")

    def view_author_details(self):
        name = input("Enter author name: ")
        for author in self.authors:
            if author.get_name() == name:
                author.display_info()
                return
        print("Author not found.")

    def display_all_authors(self):
        if not self.authors:
            print("No authors available.")
        for author in self.authors:
            author.display_info()




library = Library()
library.main()