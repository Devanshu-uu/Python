a=(1,2,4,5,6,7)
b=()

c=(1) #it is integer not tuple
print(type(c))

d=(1,) #it is tuple
print(type(d))


print(a[1])
print(a[-1])

print(a[1:3]) # last index not include

print(4 in a)
print(0 in a)
print(0 not in a)

print(sum(a))


print(a.count(0))

print(a.index(2)) #first occorance only

student=("Raj", 34, "Delhi")
# unpackaging
name,age,city=student 
print(name)
print(age)
print(city)

name,age,city=("Raj", 34,"Delhi")
print(name)
print(age)
print(city)

#packaging

def show():
    return 3,7
a=show()
print(show()) #As Tuple 
print(a)
