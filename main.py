from array_api import Array

###################
# MAIN


def main():
    a = Array()
    a.add("BUTTS")
    a.add("OOOH 1")
    a.add("OOOH 3")
    a.add("BUTTS")
    print(a.data)
    print(a.size)
    a.insert(2, "OOOH 2")
    print(a.data)
    a.set(0, 1)
    a.set(4, 5)
    a.debug_print()

    # print(a.data)
    # a.set(0, "Hello")
    # a.set(1, "world!")
    # print(a.data)
    # print(a.get(0))
    # print(a.get(1))


main()
