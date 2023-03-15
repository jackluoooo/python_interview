# 新式类和旧式类

# 旧式类(经典类)深度优先的例子 python 可以是多继承的
class A():
    def foo1(self):
        print("A")


class B(A):
    def foo2(self):
        pass


class C(A):
    def fool(self):
        print("C")


class D(B, C):
    pass


d = D()
d.fool()

# 新式类 继承Object 采用广度优先遍历查找方法和属性
