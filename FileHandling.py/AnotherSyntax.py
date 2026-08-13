with open ("sample1.txt","w") as file:
    file.write("Hi Buddy\n")
with open ("sample1.txt","a") as file:
    file.write("Hi Buddy\n")

with open ("sample1.txt","r") as file:
    print(file.read())

