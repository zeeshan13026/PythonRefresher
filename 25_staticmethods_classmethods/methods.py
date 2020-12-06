class ClassTest:
    def instance_method(self):
        print(f"called instance method of {self}")

    @classmethod
    def class_method(cls):
        print(f"called class method of {cls}")

    @staticmethod
    def static_method():
        print(f"called static method")

classTest = ClassTest()
classTest.instance_method()
ClassTest.class_method()
ClassTest.static_method()