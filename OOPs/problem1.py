class Student():
    def __init__(self, name ,age,city):
        self.name=name
        self.age=age
        self.city=city

s1=Student("Devanshu",21,"Delhi")
s2=Student("Gulshan",23,"Delhi")
s3=Student("Aditya",22,"UP")

print(s1.name,s2.name,s3.name)
print(s1.age,s2.age,s3.age)
print(s1.city,s2.city,s3.city)