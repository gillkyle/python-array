from array_api import Array
import csv

###################
# MAIN
a = []


def array_runner(command, arg1, arg2):
    if arg1.isdigit():
        arg1 = int(arg1)
    if arg2.isdigit():
        arg2 = int(arg2)
    if command == 'CREATE':
        global a
        a = Array()
    elif command == 'DEBUG':
        a.debug_print()
    elif command == 'ADD':
        a.add(arg1)
    elif command == 'SET':
        a.set(arg1, arg2)
    elif command == 'GET':
        a.get(arg1)
    elif command == 'DELETE':
        a.delete(arg1)
    elif command == 'INSERT':
        a.insert(arg1, arg2)
    elif command == 'SWAP':
        a.swap(arg1, arg2)
    return []


def main():
    global a
    # a = Array()
    # a.add(1)
    # try:
    #     a.insert(20, 1)
    # except Exception as e:
    #     print("Error: {}".format(e))
    # a.add("BUTTS")
    # a.add("OOOH 1")
    # a.add("OOOH 3")
    # a.add("BUTTS")
    # print(a.data)
    # print(a.size)
    # a.insert(2, "OOOH 2")
    # print(a.data)
    # a.set(0, 1)
    # a.set(4, 5)
    # a.swap(0, 4)
    # a.debug_print()
    # a._check_decrease()
    # a.debug_print()
    # a._check_decrease()
    # a.debug_print()

    with open("data.csv", "r") as file:
        reader = csv.reader(file, delimiter="\t")
        for i, line in enumerate(reader):
            commands = line[0].split(',')
            try:
                array_runner(commands[0], commands[1], commands[2])
            except Exception as e:
                print("Error {}: {}".format(i, e))


def test():
    b = Array()
    b.debug_print()
    b.add('o')
    b.add('o')
    b.add('o')
    b.add('o')
    b.add('o')
    b.add('o')
    b.add('o')
    b.add('o')
    b.add('o')
    b.add('Y')
    b.debug_print()
    b.add('P')
    b.debug_print()


main()
# test()
