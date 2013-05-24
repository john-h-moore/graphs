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

def dfs_dest(G, start, end, marked, explored):
	marked[start] = True
	for neighbor in G.nodes[start].neighbors:
		if G.nodes[start].neighbors[neighbor] not in explored:
			if neighbor not in marked:
				explored.append(G.nodes[start].neighbors[neighbor][0])
				if neighbor == end:
					marked[end] = True
					return marked, explored
				dfs_dest(G, neighbor, end, marked, explored)
	return None