name={'name': 'Devanshu', 'age': 20, 'city': 'Delhi'}

for keys in name.keys():
    print(keys)
for i in range(11):
    print("-",end=" ")
print()

for values in name.values():
    print(values)

for i in range(11):
    print("-",end=" ")
print()


for keys in name.keys():
    print(name[keys])

for i in range(11):
    print("-",end=" ")
print()

for elem in name.items():
    print(elem)
for elem in name.items():
    print("Key: ",elem[0]," , value: ", elem[1])
