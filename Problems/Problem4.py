s=input("Enter names : ")
sl=s.lower()

vowels=0
Cons=0
Digit=0
space=0



for char in sl:
    if char in "aeiou":
        vowels+=1 
    elif char >="a" and char<="z":
        Cons+=1
    elif char>="0" and char<="9":
        Digit+=1
    elif char ==" ":
        space+=1
        
print(vowels)
print(Cons)
print(Digit)
print(space)
