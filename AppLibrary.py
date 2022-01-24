
"""
Library Application using Object Oriented Programming
Functionalities:
   - display book
   - lend book - (also display the name of the person who owns the book if not present)
   - Donate a book
   - return book
"""
class Library:
    lentbooks = {}
    def __init__(self, listofbooks, library_name):
        self.listofbooks = listofbooks
        self.library_name = library_name


    def write(self):        # function to write the records of book and lender in a txt file
        self.booklib = open("library.txt", "w+")
        for item in self.listofbooks:
            if item in self.booklib.readline():
                return None
            else:
                self.booklib.write(item)
        self.booklib.close()
        return self.booklib

    def displaybook(self):  # displays the name of the books available to lend
        # self.write()
        self.booklib = open("library.txt", "r+")
        self.books = self.booklib.readlines()
        print(f"Books in {self.library_name} are displayed below:")
        for i in range(len(self.books)):
            print(f"{i+1}. {self.books[i].strip()}")
        return self.books

    def lendbook(self):     # function to lend a book from the available books
        self.displaybook()
        self.opt = int(input("Enter serial no of the book to issue or \"0\" to go back: : "))
        if self.opt == 0:
            return None
        self.user = open("lentbooks.txt", "w+")
        self.username = input("Enter your name: ")
        self.lentdata = [self.username, " : ", self.books[self.opt-1]]
        self.user.writelines(self.lentdata)
        print(f"{self.books[self.opt-1]} is issued for {self.username}")
        del self.books[self.opt-1]
        with open("library.txt", "w") as f:
            f.writelines(self.books)
        return self.books

    def addbook(self):    # funstion to add/donate a book to the library
        self.book = input("Enter the name of the book you wish to add or \"#\" to go back: : ")
        if self.book in self.listofbooks:
            print(f"{self.book} is already in our database\n")
        elif self.book == "#":
            return None
        else:
            self.listofbooks.append(self.book)
            self.write()
            print("\nThanks!! your book has been added in our library")
        return self.listofbooks

    def returnbook(self):  # function to submit the book
        self.ret = input("Enter your username or \"#\" to go back: ")
        with open("lentbooks.txt", "r") as f:
            self.lentname = f.readlines()
        count = 0
        for item in self.lentname:
            l = item.split(" : ")
            if l[0] == self.ret:
                self.retbook = l[1]
                # self.lentname.remove(item)
                break
            else:
                continue

        print(f"Book issued in your name is {self.retbook}")
        self.act = input("Press \"y\" if you want to return and \"n\" for no: ")
        if self.act == "y":
            with open("library.txt", "a+") as f:
                f.write(self.retbook)
        # if self.ret in self.lentbooks.values():
        #     self.listofbooks.append(self.ret)
            print("Your book is successfully returned")
        else:
            return None
        # with open("lentbooks.txt", "w") as f:
        #     f.writelines(self.lentname)

info = Library(['21\n', '309\n', '506\n', '310\n', '410\n'], "Shikhar's Library")
# action = Library()

def menu():
    menu = ["Display books", "Issue book(s)", "Donate book(s)", "Return book", "Exit"]
    for i in range(len(menu)):
        print(f"{i + 1}. {menu[i]}")

def lib():
    opt = 0
    print("Welcome to Shikhar's Library\n")
    while opt != 5:
        menu()
        opt = int(input("\nChoose any serial number: "))
        if opt == 1:
            info.displaybook()
        elif opt == 2:
            info.lendbook()
        elif opt == 3:
            info.addbook()
        elif opt == 4:
            info.returnbook()
        elif opt == 5:
            opt == 5
        else:
            print("choose correct number")
            continue
        opt = input("\nPlease press \"M\" to return to menu or press \"E\" for exit")
        if opt == "m":
            continue
        if opt == "E":
            opt = 5

if __name__ == '__main__':
    lib()

