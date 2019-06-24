import pandas as pd
import pprint as pprint
import random as random
import networkx as nx
import matplotlib as mpl

player_data = pd.read_csv("fifa_19_player_data.csv", encoding="latin-1",low_memory = False)

players = player_data["Player Name"]
clubs = player_data["Club"]
leagues = player_data["League"]
nationalities = player_data["Nationality"]
positions = player_data["Position"]

formation_442 = ["GK","RB","CBR","CBL","LB","RM","CMR","CML","LM","STR","STL"]

graph_442 = nx.Graph()

graph_442.add_nodes_from(formation_442)

#print(list(graph_442.nodes()))

graph_442.add_edges_from([("GK","CBL"),("GK","CBR"),
						  ("CBL","LB"),("CBL","CBR"),("CBL","CML"),
						  ("LB","LM"),
						  ("CML","LM"),("CML","STL"),("CML","CMR"),
						  ("LM","STL"),
						  ("CBR","RB"),("CBR","CMR"),
						  ("RB",'RM'),
						  ("CMR","RM"),("CMR","STR"),
						  ("RM","STR"),
						  ("STL","STR")])
#print(list(graph_442.edges()))

# for node in graph_442.nodes():
# 	


# for player in formation_442:
i = 0
list_len = players.size
#x = random.randint(1,list_len)
for x,y in graph_442.adj.items():
	print(x,y)
for position in formation_442:
	x = random.randint(1,list_len)
	while position[:2] != positions[x]:
		x = random.randint(1,list_len)
		
	graph_442.nodes[position]['Player'] = players[x]
	graph_442.nodes[position]['Club'] = clubs[x]
	graph_442.nodes[position]['League'] = leagues[x]
	graph_442.nodes[position]['Nationality'] = nationalities[x]
	graph_442.nodes[position]['Position'] = positions[x]


# pprint.pprint(list(graph_442.nodes.data()))

# for x,y in graph_442.adj.items():
	# print(x,y)
# print(nx.info(graph_442))

for a,b in graph_442.nodes.data():
	print(a,b)