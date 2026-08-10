students= [{'roll': 101, 'name': 'Rahul', 'age': 20, 'course': 'Python', 'marks': 85},
{'roll': 102, 'name': 'Neha', 'age': 19,  'course':'SQL', 'marks': 92},
{'roll': 103, 'name': 'Amit', 'age': 22, 'course': 'Python', 'marks': 74},
{'roll': 104, 'name': 'Priya', 'age': 21, 'course': 'AI', 'marks': 96} ,
{'roll': 105, 'name': 'Rohan', 'age': 20, 'course': 'Python', 'marks': 67}]





        
class Student:
    def __init__(self,roll,name,age,course,marks):
        self.roll=roll
        self.name=name
        self.age=age
        self.course=course
        self.marks=marks

    def show(self):
        print(self.roll,self.name,self.age,self.course,self.marks)


s1=Student(106 ,"Dev",21,"Code",100)

s1.show()

