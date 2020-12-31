class Foo:
    def __init__(self):
        self.text = input("Enter some text: ")
    def __mul__(self, other):
        a = Foo()
        a.text = self.text + other.text
    def __str__(self):
        print(self.text[::-1])
