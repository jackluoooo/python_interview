# 类变量和示例变量
class Test(object):
    num_of_instance = 0

    def __init__(self, name):
        self.name = name
        Test.num_of_instance += 1


class Person:
    name = []


if __name__ == '__main__':
    # print(Test.num_of_instance)
    # t1 = Test('jack')
    # print(Test.num_of_instance)
    # t2 = Test('lucy')
    # print(t1.name, t1.num_of_instance)
    # print(t2.name, t2.num_of_instance)
    p1 = Person()
    p2 = Person()
    p1.name.append(1)
    print(p1.name)
    print(p2.name)
    print(Person.name)
