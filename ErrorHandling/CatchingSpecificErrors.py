
# try:
#     a=int(input("Enter a: "))
#     b=int(input("Enter b: "))
#     print(a/b)
# except Exception as e:
#     print(e)



try:
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    print(a/b)
except ZeroDivisionError:
    print("Division by zero is not allowed ")
except ValueError:
    print("Enter numbers only")

except Exception as e:
    print("Some error has occured")