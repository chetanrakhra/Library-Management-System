# Create Library class
# display book
# lend book - who owns the book if not available
# add book
# return book

# Chetan Library = Library(listofbooks, library_name)

# Dictionary- (Books-nameofperson)

# Create a main function and run an infinite while loop asking users for their input

class Library:
    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lendDict = {}

    def displaybooks(self):
        print(f"We have following books in our Library: {self.name}")
        for book in self.bookslist:
            print(book)

    def lendbook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated... You can take the book now")
        else:
            print(f"Book is allready being used by {self.lendDict[book]}")

    def addbook(self, book):
        self.bookslist.append(book)
        print("Book has been added to the book list")

    def returnbook(self, book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    chetan = Library(['Python', 'Rich Dad poor Dad', 'Harry Potter', 'C++ Basic', 'Algorithms by CLRS'], "CodeWithChetan")


    while('true'):
        print(f"Welcome to the {chetan.name} library. Enter your choice to continue")
        print("1. Display Book")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")
        user_choice = (input())
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option...")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            chetan.displaybooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name:")
            chetan.lendbook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            chetan.addbook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            chetan.returnbook(book)

        else:
            print("Enter a valid input")

        print("Press q to quit and press c to continue")
        user_choice2 = input()
        if user_choice2 == "q":
            exit()

        elif user_choice2 == "c":
            continue

        else:
            print("Enter a valid input")