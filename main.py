class Messanger():

    a = 12


class A():

    def __init__(self, m):
        self.m = m

    def changeA(self):
        self.m.a = 7

class B():

    def __init__(self, m):
        self.m = m

    def changeA(self):
        self.m.a = 9

m = Messanger()
a = A(m)
b = B(m)

print b.m.a
a.changeA()
print b.m.a
b.changeA()
print a.m.a