upper_case=False
lower_case=False
digit=False
password=input("Enter Password: ")


for c in password:
    if c >="A" and c<="Z":
        upper_case=True
    elif c >="a" and c<="z":
        lower_case=True
    elif c >="0" and c<="9":
        digit=True
if (len(password)>=8 and upper_case and lower_case and digit):
    print("Strong Password")
else:
    print("Weak Password")