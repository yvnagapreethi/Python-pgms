class Cirlce:

    def __init__(self):
        self.radius = float(input("Please enter the radius value to find the area of a cirlce:::"))

    def get_area(self):
        return 3.14 * self.radius**2
        # print("The radius is {0}".format(radius))


if __name__== "__main__":
    my_circle = Cirlce()
    print("The area of a circle is:{0} ".format(my_circle.get_area()))
