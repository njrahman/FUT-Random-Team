import pandas as pd
import pprint as pprint
import random as random


player_data = pd.read_csv("fifa_19_player_data.csv", encoding="latin-1")

players = player_data["Player Name"]
clubs = player_data["Club"]
leagues = player_data["League"]
nationalities = player_data["Nationality"]
positions = player_data["Position"]
player_info = {}

i = 0

while i < players.size:
   player_info[players[i]] = [clubs[i],nationalities[i],leagues[i],positions[i]]
   i+=1

x = random.randint(1,players.size)
player = players[x]

formation_442 = ["GK","RB","CB","CB","LB","RM","CM","CM","LM","ST","ST"]
team = {}
for position in formation_442:
   print(position)
   x = random.randint(1,players.size)
   player = players[x]
   while player_info[player][3] != position:
      x = random.randint(1,players.size)
      player = players[x]
   team[player] = player_info[player] 
   print(player_info[player])
pprint.pprint(team)