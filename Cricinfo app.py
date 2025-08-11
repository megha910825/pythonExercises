## You are building the Cricinfo app. As you are admin of the app
## Enter the name of the player and runs they scored.

# When a user comes in to check the scores, he will be asked 
# to enter the name of the player and you will return the runs
# that specific player scored

# player_info= { "kohli":50, "sharma": 24, "cde" : 33, "fgh": 44}
scores = {}
for i in range(5):
    name = input("Enter the name of the player::")
    run = int(input("Enter the runs scored::"))
    scores[name]= run

print(scores)

key = input("Enter the player name::")
print(scores[key])
