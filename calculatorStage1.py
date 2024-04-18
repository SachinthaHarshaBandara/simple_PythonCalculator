# TODO: Write the functions for arithmatic operations here
# These functions should cover Task 2

def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def devide(a, b):
    try:
        return a/b
    except Exception as e:
        print(e)


def power(a, b):
    return a**b


def remainder(a, b):
    return a % b
# -------------------------------------
# TODO: Write the select_op(choice) function here
# This function sould cover Task 1 (Section 2) and Task 3


def select_op(choice):
    if (choice == '#'):
        return -1
    elif (choice == '$'):
        return 0
    elif (choice in ('+', '-', '*', '/', '^', '%')):
        while (True):
            n1 = input('Enter first number: ')
            print(n1)
            if n1.endswith('$'):
                return 0
            if n1.endswith('#'):
                return -1
            try:
                m1 = float(n1)
                break
            except:
                print('Not a valid number, please enter again')
                continue

        while (True):
            n2 = input('Enter second number: ')
            print(n2)
            if n2.endswith('$'):
                return 0
            if n2.endswith('#'):
                return -1
            try:
                m2 = float(n2)
                break
            except:
                print('Not a valid number, please enter again')
                continue

        if (choice == '+'):
            print(m1, '+', m2, '=', add(m1, m2))
        elif (choice == '-'):
            print(m1, '-', m2, '=', subtract(m1, m2))
        elif (choice == '*'):
            print(m1, '*', m2, '=', multiply(m1, m2))
        elif (choice == '/'):
            print(m1, '/', m2, '=', devide(m1, m2))
        elif (choice == '^'):
            print(m1, '^', m2, '=', power(m1, m2))
        elif (choice == '%'):
            print(m1, '%', m2, '=', remainder(m1, m2))


# End the select_op(choice) function here
# -------------------------------------
# This is the main loop. It covers Task 1 (Section 1)
# YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    if (select_op(choice) == -1):
        # program ends here
        print("Done. Terminating")
        exit()
