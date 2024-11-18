class dog:
    def a(self):
        print("This is dog")

class horse:
    def b(self):
        print("this is horse")

class animal(dog,horse):
    pass

ss = animal()
ss.a()
ss.b()
