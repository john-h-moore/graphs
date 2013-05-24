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
	explored = []
	while queue:
		curr = queue.pop()
		for neighbor in G.nodes[curr].neighbors:
			if neighbor not in marked:
				marked[neighbor] = True
				explored.append(G.nodes[curr].neighbors[neighbor][0])
				queue.append(neighbor)
	return marked, explored

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

def bfs_dest(G, start, end, marked):
	queue = [start]
	marked[start] = True
	explored = []
	while queue:
		curr = queue.pop()
		for neighbor in G.nodes[curr].neighbors:
			if neighbor not in marked:
				marked[neighbor] = True
				explored.append(G.nodes[curr].neighbors[neighbor][0])
				if neighbor == end:
					return marked, explored
				queue.append(neighbor)
	return None

def return_path(explored, start, end, path):
	for edge in explored:
		if end in edge.label[1]:
			path.append(edge)
			n = edge.label[0]
			if n == start:
				return path
			explored.pop(explored.index(edge))
			return_path(explored, start, n, path)
	return path

def find_path(explored, start, end):
	path = []
	return_path(explored, start, end, path)
	path.reverse()
	return path

def format_path(path):
	p = ''
	for edge in path:
		p += edge.label[0] + ' --> '
	return p + path[-1].label[1]