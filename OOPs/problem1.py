class Student():
    def __init__(self, name ,age,city):
        self.name=name
        self.age=age
        self.city=city
    def display(self):
        print(self.name,self.age,self.city)


        

s1=Student("Devanshu",21,"Delhi")
s2=Student("Gulshan",23,"Delhi")
s3=Student("Aditya",22,"UP")


s1.display()
s2.display()
s3.display()
