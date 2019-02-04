class Cirlce:

    def __init__(self):
        self.radius = float(input("Please enter the radius value to find the area of a cirlce"))
        print("The area of a circle is:{0} ".format(self.area1(self.radius)))

    def area1(self, radius):
        return 3.14 * self.radius**2
        # print("The radius is {0}".format(radius))


Cirlce()
