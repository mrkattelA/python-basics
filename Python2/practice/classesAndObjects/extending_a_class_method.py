class A:
    def __init__(self, name):
        self.name = name

    def intro(self):
        print("Hello, my name is {}".format(self.name))

    def outro(self):
        print("GoodBye")

class B(A):
    def intro(self):
        super().intro()
        print("it's nice to meet you. ")

a = A("Alpha")
b = B("Beta")

a.intro()
b.intro()
a.outro()
b.outro()

