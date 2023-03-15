# python 里的元类
# MetaClass 本质也是一个类，它可以对类内部的定义(包括类属性和类方法) 进行动态的修改。可以这么说，使用元类的主要目的就是为了在实现创建类时，能够动态的改变类的属性和方法

class FirstMetaClass(type):
    # cls代表动态修改的类
    # name代表动态修改的类名
    # bases代表被动态修改的类的所有父类
    # attr代表被动态修改的类的所有属性、方法组成的字典
    def __new__(cls, name, bases, attrs):
        attrs['name'] = "C语言中文网"
        attrs["say"] = lambda self: print("调用say()方法示例")
        return super().__new__(cls, name, bases, attrs)


class CLanguage(object, metaclass=FirstMetaClass):
    pass


clanguage = CLanguage()
clanguage.say()
print(clanguage.name)
