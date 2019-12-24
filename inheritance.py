class book:
    def __init__(self):
        print("parent")
class text(book):
    def __init__(self):
        print("child")
        super().__init__()
b=text()


