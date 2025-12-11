class A :
    def show(laxman,m1):
        laxman.m1= m1 
        print("it my phone")
        print("it new phone")

class B(A):
     def show(laxman):
        super().show(laxman)
        print("it my second phone")
    

c1=B()
c1.show()
