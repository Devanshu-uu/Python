s="Python is the most amazing programing language for ML today"

freq={}

for c in s:
    if c!=" ":
        if c not in freq:
            freq[c]=1
        else:
            freq[c]+=1
print(freq)
max_v=0


for k,v in freq.items(): 
    if v>max_v:
        max_v=v
        max_k=k

print(f'{max_k}, {max_v}')

