import networkx as nx
import matplotlib.pyplot as plt

def draw_network(nodelist, colorfavor, wordfavor):
	"""
	function that plots the graph of nodes simulated in the Model function
	"""
	
	G = nx.Graph()
	
	plt.clf()
	
	# create graph
	G.add_nodes_from(nodelist)
	G.add_edges_from([(nodelist[0], nodelist[4]), (nodelist[0], nodelist[5]), (nodelist[1], nodelist[4]), (nodelist[1], nodelist[5]),
					(nodelist[2], nodelist[6]),(nodelist[2], nodelist[7]), (nodelist[3], nodelist[6]), (nodelist[3], nodelist[7]), 
					(4, nodelist[4]), (4, nodelist[5]),(5, nodelist[6]),
					(5, nodelist[7]),(nodelist[4], nodelist[8]), (nodelist[4], nodelist[9]), (nodelist[5], nodelist[8]),
					(nodelist[5], nodelist[9]), (nodelist[6], nodelist[8]), (nodelist[6], nodelist[9]), (nodelist[7], nodelist[8])
					, (nodelist[7], nodelist[9])])
	
	firingnodes = []
	notfiringnodes = []
			
	# create dictionary of node locations
	Pos = {nodelist[0]: (.20,.20), nodelist[1]: (.30,.20), 4: (.40,.20), 5: (.50,.20), 
			nodelist[2]: (.60,.20), nodelist[3]: (.70,.20), nodelist[4]: (.20,.40), nodelist[5]: (.30,.40), 
			nodelist[6]: (.60,.40),nodelist[7]: (.70,.40), nodelist[8]: (.40,.60), nodelist[9]: (.50,.60)}
	
	
	#gotta append the instruction nodes
	nodelist.append(4)
	nodelist.append(5)
	
	#plot network (in future versions I would like to have the network display the most
	#active nodes, but networkx plotting is very finicky)
	nx.draw_networkx_nodes(G, Pos, nodelist, node_color = "b")
	nx.draw_networkx_edges(G, Pos)

	plt.annotate("Red Color", xy = (.15,.15), color = "red")
	plt.annotate("Grn Color", xy = (.25,.15), color = "green")
	plt.annotate("Say Ink", xy = (.35,.15))
	plt.annotate("Say Word", xy = (.45,.15))
	plt.annotate("Red Word", xy = (.55, .15), color = "red")
	plt.annotate("Blue Word", xy = (.65, .15), color = "green")
	plt.annotate("RED", xy = (.38, .65), color = "red")
	plt.annotate("GREEN", xy = (.47, .65), color = "green")
	
	plt.show()
	plt.draw()

