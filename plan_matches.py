import collections
import sys



#Read and check parse arguments
if (len(sys.argv)!= 2):
	print("You should parse a single graph representation file as parameter!")
	sys.exit(0)
'''
We are asked to process graph data in the  order that we read them
So we are going to use an OrderedDict()
'''
graph = {}

#Read graph data and store to dictionary
with open(sys.argv[1], "r") as file:
	for line in file:
		splittline = line.strip("\n").split(" ")
		try:
			graph[splittline[0]].append(splittline[1])
		except KeyError:

			graph[splittline[0]]=[splittline[1]]

#make graph repesentation summetric	
graph_copy = graph.copy()		
for node,adj_nodes in graph_copy.items():
	for ad_node in adj_nodes:
		if (ad_node not in graph):
			graph[ad_node]=[node]
		elif (node not in graph[ad_node]):
			graph[ad_node].append(node)

#Compute graph's max degree node
max_degree = 0
for k,v in graph.items():
	if len(v) > max_degree:
		max_degree = len(v)

#set availiable color to 2*max_node_degree
max_colors = range(2*max_degree)

#Keep track for already assigned game days for each node player
node_colors = {}
for k in graph.keys():
	node_colors[k] = []



#Order graph dictionary by key
ordered_graph = collections.OrderedDict(sorted(graph.items()))

#Greedy algorithm for scheduling
schedule = {}
for node,adj_nodes in ordered_graph.items():	
	for ad_node in sorted(adj_nodes):
		if (((node,ad_node) not in schedule) and ((ad_node,node)not in schedule)):
			availiable_days = list(set(max_colors).difference(set(node_colors[node]),set(node_colors[ad_node])))
			min_day = min(availiable_days)
			node_colors[node].append(min_day)
			node_colors[ad_node].append(min_day)
			schedule[(min(node,ad_node),max(node,ad_node))] = min_day
		else:
			continue

ordered_schedule = collections.OrderedDict(sorted(schedule.items()))

#print shorted schedule
for k,v in ordered_schedule.items():
	print(k,v) 

	
'''
Note--> For the example_graph_3.txt graph our algorithm produces a feasible
solution(no player plays more than one game per day)  using 1 less day
(6 instead of 7) compared to example_graph_3_solved.txt

'''