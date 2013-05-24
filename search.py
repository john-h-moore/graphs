import graphs

def dfs(G, v, marked, explored):
	marked[v] = True
	for neighbor in G.nodes[v].neighbors:
		if G.nodes[v].neighbors[neighbor] not in explored:
			if neighbor not in marked:
				explored.append(G.nodes[v].neighbors[neighbor][0])
				dfs(G, neighbor, marked, explored)
	return marked, explored

def bfs(G, v, marked):
	queue = [v]
	marked[v] = True
	while queue:
		w = queue.pop()
		for neighbor in G.nodes[w].neighbors:
			if neighbor not in marked:
				marked[neighbor] = True
				queue.append(neighbor)
	return marked