# Introductory Python Course 2021 - UiT
# By Brett Alistair Kromkamp (brettkromkamp@gmail.com - https://brettkromkamp.com)


def foo():
    print("begin")
    for i in range(3):
        print("before yield", i)
        yield i
        print("after yield", i)
    print("end")


f = foo()
print("Before next #1")
next(f)
print("After next #1")
print("Before next #2")
next(f)
print("After next #2")
print("Before next #3")
next(f)
print("After next #3")
