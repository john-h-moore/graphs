import random
import string

class Node:
	def __init__(self, label):
		self.label = label
		self.neighbors = {}
		self.data = None
	def add_neighbor(self, edge):
		self.neighbors[edge.end.label] = (edge, edge.end)
	def node_data(self, data):
		self.data = data

class Graph:
	def __init__(self, name='G'):
		self.name = name
		self.nodes = {}
		self.edges = {}
	def add_node(self, node):
		self.nodes[node.label] = node
	def edge(self, node1, node2, directed = False, weight = None):
		# n = (node1, node2)
		# self.edges[(n[0].label, n[1].label)] = n
		if node1 == node2 and directed == False:
			return
		e = Edge(node1, node2, directed, weight)
		if directed == False:
			e2 = Edge(node2, node1, directed, weight)
			self.edges[e2.label] = e2
		node1.add_neighbor(e)
		if directed == False:
			node2.add_neighbor(e2)
		self.edges[e.label] = e
	def populate_graph(self, numnodes=20):
		for i in range(numnodes):
			l = random.choice(string.ascii_lowercase)
			n = Node(l)
			self.add_node(n)
	def link_graph(self):
		for i in range(len(self.nodes)):
			if random.randint(1, 10) %3 == 0:
				self.edge(self.nodes[random.choice(self.nodes.keys())], self.nodes[random.choice(self.nodes.keys())])
	def generate_rand_graph(self, numnodes=20, linkiters=4):
		self.populate_graph(numnodes)
		for i in range(linkiters):
			self.link_graph()
	def rand_node(self):
		return random.choice(self.nodes.keys())

class Edge:
	def __init__(self, start, end, directed=False, weight=None):
		assert type(start), type(end) == Node
		self.start = start
		self.end = end
		self.directed = directed
		self.weight = weight
		self.label = (start.label, end.label)