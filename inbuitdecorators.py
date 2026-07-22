#  Class Method
class Student:
    college = "ABC College"

    @classmethod
    def show_college(cls):
        print("College:", cls.college)

Student.show_college()

#Static Method
class Math:

    @staticmethod
    def add(a, b):
        print("Sum =", a + b)

Math.add(5, 7)
