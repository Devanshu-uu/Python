class People:
    def __init__(self,FirstName,LastName):
        self.FirstName=FirstName
        self.LastName=LastName

    def show(self):
        print(self.FirstName,self.LastName)
p1=People("Devanshu","Mohriya")

p1.show()


class Student(People):
    pass

s1=Student("Gulshan","Mohriya")

s1.show()


        