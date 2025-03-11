class A:
    def __init__(self, name):
        self.name = name

    def intro(self):
        print("Hello my name is {}".format(self.name))

    def outro(self):
        print("Goodbye")

class B(A):
    def intro(self):
        print("Hi, {}, How are you doing".format(self.name))

a = A("MIKE")
b = B("ARNOLD")
a.intro()
b.intro()
a.outro()
b.outro()