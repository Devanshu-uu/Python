players={"virat":32,
         "dhoni":200,
         "hardik":40,
         "Bumra":78}
max_score=0
max_player=""
min_player=""
min_score=10000
total_score=0

# for i in range(5):
#     name=input("Enter Name: ")
#     runs=int(input("Enter Name: "))

for key in players:
    total_score+=players[key]
    if(players[key]>max_score):
        max_score=players[key]
        max_player=key
    if(players[key]<min_score):
        min_score=players[key]
        min_player=key


print(f'{max_player},{max_score}')
print(f'{min_player},{min_score}')
print(total_score/len(players))

