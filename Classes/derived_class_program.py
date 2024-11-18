class parent_1:
    def fun_1(self):
        print("This is function in parent class")
    class child_1:
        def fun_2(self):
            print("This function is called inside the child class")


p = parent_1()
c = p.child_1()
c.fun_2()
