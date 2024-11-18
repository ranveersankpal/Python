class first:
    s = "sankpal"

class second(first):
    def yash(self):
        print("This is Yash",self.s)
        r = "This is Yash"+self.s

class third(second,r):
    def greeting(self): self.r=r
        print("Hello",self.r)


ss= second()
ss.yash()

