# python 的函数传递
a = 1


def fun(a):
    print("func_in", id(a))
    a = 2
    print("re-point", id(a), id(2))


print("func_out", id(a), id(1))

fun(a)
print(a)

b = []


def funb(b):
    print("func_in", id(b))
    b.append(1)
    print("func_out", id(b))


# print("func_out", id(b))
funb(b)
print(b)
