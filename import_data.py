import pandas as pd
import pprint as pprint
import random as random

player_data = pd.read_csv("fifa_player_data.csv")

players = player_data["Name"]
clubs = player_data["Club"]
nationalities = player_data["Nationality"]
positions = player_data["Position"]
player_info = {}

i = 0

while i < players.size:
   player_info[players[i]] = [clubs[i],nationalities[i],positions[i]]
   i+=1

#print(player_info.items())

print(random.randint(1,players.size))

#pprint.pprint(player_data)