# class ils:
#     def python(self):
#         print("This is python class")
#     def java(self):
#         print("This is java class")
#     def dotNet(self):
#         print("This is dotNet class")

# i=ils()
# i.python()
# i.java()
# i.dotNet()



## INHERITENCE #######   
### Multiple inheritecne #####

class A:
    def a(self):
        print("This is class A")
class B:
    def b(self):
        print("This is class B")

class C(A,B):
    def c(self):
        print("This is class C")
m=C()
m.a()
m.b()

class D:
    def a(self):
        print("This is class Faheem")
class E(D):
    def b(self):
        print("This is class Wasiq")
class F(E):
    def c(self):
        print("This is class Towheed")
k=F()
k.b()
k.a()
k.c()


