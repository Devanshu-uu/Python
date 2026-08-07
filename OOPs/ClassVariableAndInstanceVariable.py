class Student:
    college= "IIT BOMBAY"

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name, self.age)


s1=Student("Devanshu",21)

s1.show()

print(s1.college)