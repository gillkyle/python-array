from array_api import Array
import csv

###################
# MAIN
a = []


def array_runner(command, arg1, arg2):
    global a

    if arg1.isdigit():
        arg1 = int(arg1)
    if arg2.isdigit():
        arg2 = int(arg2)
    if command == 'CREATE':
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

    with open("data.csv", "r") as file:
        reader = csv.reader(file, delimiter="\t")
        for i, line in enumerate(reader):
            commands = line[0].split(',')
            try:
                array_runner(commands[0], commands[1], commands[2])
            except Exception as e:
                print("Error {}: {}".format(i, e))


main()
