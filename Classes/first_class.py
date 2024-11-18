class demo:
    def __init__(self,a):
        print("This is a constructor")
        self.a=a
        print("value of a is : ",self.a)
    def __del__(self):
        print("This is a desctructor")

d=demo(5)

