#Types of Methods

class Demo:

    def instance_method(self):
        print("This is an Instance Method")

    @classmethod
    def class_method(cls):
        print("This is a Class Method")

    @staticmethod
    def static_method():
        print("This is a Static Method")

obj = Demo()

obj.instance_method()
Demo.class_method()
Demo.static_method()
