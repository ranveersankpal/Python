class first:
    s = "sankpal"

class second(first):
    def yash(self):
        print("This is Yash",self.s)
        r = "This is Yash"+self.s

class third(second):
    def greeting(self):
        super().yash()
        print("Hello")


ss= third()
ss.greeting()

