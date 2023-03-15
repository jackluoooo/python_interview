# *args and **kwargs
def print_everything(*args):
    for index, val in enumerate(args):
        print(index, val)


print_everything("A", "C")


def table_thing(**kwargs):
    for name, value in kwargs.items():
        print(f"{name}={value}")


table_thing(apple="fruits", cabbage="vegetable")

# args 必须在 **kargs 的前面
myList = ['A', 'B', 'C']
print(*myList)
