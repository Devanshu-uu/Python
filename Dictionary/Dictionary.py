student={
    "name" : "Devanshu",
    "age" : 21
}


print(student)

print(type(student))
print(student["name"])
print(student["age"])


print(student.keys())
print(student.values())

student["age"]=20;
print(student)
student["city"]="Delhi"
print(student)

# print(student["Age"]) // case sensitive

print(student.get("age","Key not found"))
print(student.get("Age","Key not found"))

student.pop("city")
print(student)
