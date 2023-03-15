# python 切面编程 装饰器是把其他的函数作为参数的函数

# 手动实现装饰器
def my_new_decorator(a_function_to_decorate):
    def the_wrapper_function():
        print("Before the function runs")
        a_function_to_decorate()
        print("After the function runs")

    return the_wrapper_function  # 返回包装后的函数


def a_stand_alone_function():
    print("I am a stand alone function , don't you dare modify me")


# a_stand_alone_function()
# dec = my_new_decorator(a_stand_alone_function)
# dec()


@my_new_decorator
def another_stand_alone_function():
    print("Leave me alone")


# another_stand_alone_function()

# 在迭代器中传入参数
def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print("I got args! Look:", arg1, arg2)
        function_to_decorate(arg1, arg2)

    return a_wrapper_accepting_arguments


@a_decorator_passing_arguments
def print_full_name(f, l):
    print("My name is", f, l)


print_full_name("Peter", "Venkman")

# 将一个函数的引用作为一个参数传给另一个参数
