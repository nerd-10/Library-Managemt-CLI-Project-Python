class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0
        
    def add_books(self,book_name):#add books
        for existing_book in self.books:
            if existing_book.lower() == book_name.lower():
                print(f"Books {book_name} aleady exists!")
                return
        self.books.append(book_name)
        self.no_of_books+=1 
        print(f"Book {book_name} has been added successfully!")
    
    def show_books(self):#show books
        if (self.no_of_books == 0):
            print("No Books to show")
        
        else:
            for idx,book in enumerate(self.books,start=1):
                print(f"{idx}. {book}")
                
    def get_no_of_books(self):
        print(f"Total number of boks are:{self.no_of_books}")
        return self.no_of_books
        
        
    def remove_book(self,index):
        if 0 <=index < len(self.books):
            removed = self.books.pop(index)
            self.no_of_books-=1
            print(f"Book {removed} has been removed successfully!")
        else:
            print("Invalid index.Please type correct index!")
    
        
if __name__=="__main__":
    #harcdoced book addition
    lib = Library()
    lib.add_books("Crime and Punishment")
    lib.add_books("Naruto")
    lib.add_books("White Nights")
    lib.show_books()
    lib.get_no_of_books()
    #user input for book name
    while True:
        print("Menu")
        print("1. Add book")
        print("2. Show all books")
        print("3. Number of books")
        print("4. Remove book")
        print("5. To exit")
        
        choice = input(("Please make a choice:")).strip()
        if choice == "1":
            book_name=input("Pleae enter book name:").strip()
            if book_name:
                lib.add_books(book_name)
            else:
                print("Please entera valid book name!\n")
        
        elif choice == "2":
            lib.show_books()
        
        elif choice == "3":
            lib.get_no_of_books()
        
        elif choice == "4":
            lib.show_books()
            if lib.no_of_books>0:
                try:
                    index = int(input("Please enter the index of the book that you want to remove:"))-1
                    lib.remove_book(index)
                except ValueError:
                    print("Invalid index type")
        elif choice=="5":
            print("Exiting the program")
            break
        
        else:
            print("Please enter valid choice from the menu!")