from array_api import Array

###################
# MAIN


def main():
    a = Array()
    print(a.size)
    print(a.data)
    print(a._check_bounds(-1))
    print(a._check_bounds(9))
    print(a._check_increase())
    b = Array()
    print(b.data)


main()
