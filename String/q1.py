user=input("Enter a String: ")
small=""
for ch in user:
    n=ord(ch)
    if(n>=65 and n<=90):
        n+=32
    small+=chr(n)
  
        
print(small)
    

    