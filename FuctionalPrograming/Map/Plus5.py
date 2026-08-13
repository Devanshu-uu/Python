lst=[2,3,4,5,6]
lst1=[]
for i in lst:
    lst1.append(i+ 5)
print(lst1)


def plus(a):
    lst2=[]
    for i in a:
        lst2.append(i+5)
    return lst2

print(plus(lst))


def plus5(n):
    return n+5


lst3=[]
for i in lst:
    lst3.append(plus5(i))


print(lst3)