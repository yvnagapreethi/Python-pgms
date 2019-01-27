class MethodsOfPython:

    def __init__(self):
        print("instance method")

    @classmethod
    def class_method(cls):
        print("class method1")

    @staticmethod
    def static_method():
        print("static method")

    def inst_methond(self):
        print("calling instance method")


MethodsOfPython.static_method()
mp = MethodsOfPython()
mp.static_method()
mp.class_method()
# MethodsOfPython.inst_methond()
mp.inst_methond()
