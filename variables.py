#Local Variable
def show():
    x = 10      
    print("Local variable:", x)

show()

#Global variable
x = 100      

def display():
    print("Global variable:", x)

display()

#Class Variable and Instance Variable
class Student:
    college = "ABC College"  

    def __init__(self, name):
        self.name = name     

s1 = Student("Rahul")

print("Name:", s1.name)
print("College:", Student.college)
