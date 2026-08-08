
try:
    a=int(input("Enter a: "))
except ValueError:
    print("Invalid Input")
else:
    print(f'Input is {a}')
    
