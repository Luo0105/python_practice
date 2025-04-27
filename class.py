class Book:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print(f'You have borrowed "{self.title}".')
        else:
            print(f'Sorry, "{self.title}" is not available right now.')

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            print(f'You have returned "{self.title}".')
        else:
            print(f'All copies of "{self.title}" are already in the library.')

    def get_info(self):
        print(f'"{self.title}" by {self.author} - {self.available_copies}/{self.total_copies} available.')

# 使用这个类
book1 = Book("1984", "George Orwell", 3)

book1.get_info()
book1.borrow()
book1.get_info()
book1.borrow()
book1.borrow()
book1.borrow()  # 已经借光了
book1.return_book()
book1.get_info()
