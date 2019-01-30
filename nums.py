class Numbers:

    def __init__(self):
        self.nums = input("enter the numbers seperated by comma :")
        self.list_tuple(self.nums)

    def list_tuple(self, nums):
        self.lst = self.nums.split(",")
        print("List {0} tuple {1} :".format(self.lst, tuple(self.lst)))


if __name__ == '__main__':
    n = Numbers()
