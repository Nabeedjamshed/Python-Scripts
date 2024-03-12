class Library:
    noofbooks = 0
    def book(self):
        self.no_of_books = 0
        self.books = []
        Library.noofbooks += 1
        self.n1 = int(input(f"Enter total no of books of Libarary {self.noofbooks}: "))
        for i in range(self.n1):
            self.n2 = input("Enter the name of a book: ")
            self.books.append(self.n2)
            self.no_of_books += 1
    def show(self):
        if len(self.books) == self.no_of_books: 
            print(f"The library has {self.no_of_books} books.")
            for j in self.books:
                print(j)
        else:
            print("Invalid Code")
lib1 = Library()
lib1.book()
print("Libarary 1")
lib1.show()
lib2 = Library()
lib2.book()
print("Libarary 2")
lib2.show()
lib3 = Library()
lib3.book()
print("Libarary 3")
lib3.show()
