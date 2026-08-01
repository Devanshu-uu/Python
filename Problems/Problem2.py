# Problem 2 : Word Frequency Counter i
# Problem Statement i
# Take a sentence as input. E
# Display how many times each word appears. E
# Egl: python is fun python is easy E


s=input("Enter a sen: ")

words=s.split(" ")

freq={}

for word in words:
    if word not in freq:
        freq[word]=1
    else:
        freq[word]+=1
print(freq)
