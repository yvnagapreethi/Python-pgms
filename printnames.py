class PrintNames:

    def __init__(self):
        first = input("Enter your first name")
        last = input("Enter your last name")
        print("Final is {0} {1}".format(first[-1::-1], last[-1::-1]))


if __name__ == '__main__':
    pn = PrintNames()
