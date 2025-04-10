# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first}  {last}")
#
# hello("hello", title="Mr.", first="Spongebob", last=" thie")


def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1,2, 4, 58))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("spongebob", "squarepants")



def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="shimultala", city="krishanangar", state="west bengal", zip="741101")