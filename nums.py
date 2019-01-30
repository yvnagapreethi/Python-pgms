class Numbers:

    def __init__(self):
        self.nums = input("enter the numbers seperated by comma :")
        self.list_tuple(self.nums)

    def list_tuple(self,nums):
        self.lst = self.nums.split(",")
        print("List is {0} and tuple is {1} :".format(self.lst,tuple(self.lst)))

nm = Numbers()
