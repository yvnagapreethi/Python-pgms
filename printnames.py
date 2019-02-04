class PrintNames:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        print("Full Name is {0} {1}".format(self.first_name[-1::-1], self.last_name[-1::-1]))


if __name__ == '__main__':
    first_name = input("Enter the first name")
    last_name = input("Enter the last name")
    pn = PrintNames(first_name, last_name)
