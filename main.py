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
    a.swap(0, 4)
    a.debug_print()


main()
