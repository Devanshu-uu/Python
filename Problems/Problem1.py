# Problem 1 : Student Grade Analyzer Problem Statement E
# Write a Python program that takes marks of 5 subjects as input. i
# Your program should: i
# Store the marks in a list. i
# Calculate the average marks. i
# Find the highest and lowest marks. i
# Display the grade of all marks:
marks=[]
for i in range(5):
    user=int(input("Enter Marks: "))
    marks.append(user)
print(f'avg is {sum(marks)/len(marks)}')
print(f'max is {max(marks)}')
print(f'min is {min(marks)}')

for mark in marks:
    if(mark>=90):
        print("Grade is ","A")
    elif(mark>=75):
        print("Grade is ","B")
    elif(mark>=60):
        print("Grade is ","C")
    else:
        print("Grade is ","D")
    
