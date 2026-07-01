age= int(input("Enter your age: "))
if(age>=20):
  print("You are eligible")
else:
  print("not")

password=input("Enter Password: ")
if (password == "hello@123"):
  print("Welcome")
else:
  print("Invalid Password")

marks=float(input("Enter your marks: "))
if marks<=30:
  print("Low")
else:
  if marks >=30 and marks<=70 :
    print("Avg")
  else:
    print("High")

marks=float(input("Enter your marks: "))
if marks<=30:
  print("Low")
elif marks >=30 and marks<=70 :

  print("Avg")
else:
  print("High")

age=int(input("Enter Your Age: "))
if(age>=18):
  print("Eligible")
else:
  print("Not")

n=int(input("Enter a number: "))

if (n%2==0):
  print("Even")
else:
  print("Odd")

n=int(input("Enter a number: "))

if n>0:
  print("positive")
elif n<0:
  print("Negitive")
else:
  print("Zero")

n1=int(input("Enter a number: "))
n2=int(input("Enter a number: "))

if n1>n2:
  print(f'{n1} is Greater then {n2}')
elif n2>n1:
  print(f'{n2} is Greater then {n1}')
else:
  print("Equal")

n1=int(input("Enter a number: "))

if n1>=90:
  print("A")
elif n1>=75:
   print("B")
elif n1>=60:
   print("C")
elif n1>=40:
   print("D")
else:
  print("Fail")

n1=float(input("Enter a number: "))

if n1<18.5:
  print("Underweight")
elif n1<=24.9:
   print("Normal Weight")
elif n1<=29.9:
   print("Overweight")
else:
  print("Obese")

n=int(input("Enter a number: "))

if n%3==0 and n%5==0:
  print("It is divisible by 3 and 5")
elif(n%3==0):
  print("Divisible by 3")
elif(n%5==0):
  print("Divisible by 5")
else:
  print("Not divisible by both")


