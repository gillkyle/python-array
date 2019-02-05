from array_api import Array

###################
# MAIN


def main():
    a = Array()
    # print(a.size)
    # print(a.data)
    # print(a._check_bounds(-1))
    # print(a._check_bounds(0))
    # print(a._check_bounds(9))
    # print(a._check_increase())
    # b = Array()
    # print(a._check_decrease())
    # print(b.data)
    # print(b._check_bounds(0))
    # b.set(0, "Hello")
    # b.set(1, "world!")
    # print(b.get(0))
    # print(b.get(1))
    # print(b.get(2))
    a.add(1)
    a.add(2)
    print(a.data)
    a.set(0, "Hello")
    a.set(1, "world!")
    print(a.data)
    print(a.get(0))
    print(a.get(1))


main()
