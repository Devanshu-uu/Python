# Problem Statement 
# Take names separated by spacesRemove duplicate names while preserving the first occurrence.
#  Egl: Rahul Amit Rahul Neha 


s=input("Enter names : ")
names=s.split(" ")

unique_names=[]
for elem in names:
    if elem not in unique_names:
        unique_names.append(elem)
print(unique_names)