# file=open("sample.txt","w")
# file.write("Suraj\n")
# file.write("Shiva\n")
# file.write("Devanshu\n")
# file.close()

# file=open("sample.txt","r")
# data=file.readlines()
# print(data)
# file.close()

file= open("sample.txt","a")

file.write("Gulshan\n")

file.close()


file=open("sample.txt","r")
for line in file:
    print(line,end="")
file.close()