students=["A","B","A","C","C"]
student=[]

for i in students:
    if i not in student:
        student.append(i)
print(student)