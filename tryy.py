students= [{'roll': 101, 'name': 'Rahul', 'age': 20, 'course': 'Python', 'marks': 85},
{'roll': 102, 'name': 'Neha', 'age': 19,  'course':'SQL', 'marks': 92},
{'roll': 103, 'name': 'Amit', 'age': 22, 'course': 'Python', 'marks': 74},
{'roll': 104, 'name': 'Priya', 'age': 21, 'course': 'AI', 'marks': 96} ,
{'roll': 105, 'name': 'Rohan', 'age': 20, 'course': 'Python', 'marks': 67}]



courses=[]
for student in students:
    if (student["course"] not in courses):
        courses.append(student["course"])


print(courses)


        


