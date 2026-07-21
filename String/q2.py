user=input("Enter a String: ")
small=""
for ch in user:
    n=ord(ch)
    if(n>=97 and n<=122):
        n-=32
    small+=chr(n)
  
        
print(small)
    

    