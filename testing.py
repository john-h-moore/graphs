from graphs import *
from search import *
import time

def dest_test(test_iters = 3):
	dfsm = 0
	bfsm = 0
	dfse = 0
	bfse = 0
	dfspl = 0
	bfspl = 0
	dfs_time = 0.0
	bfs_time = 0.0
	for i in range(test_iters):
		G = Graph()
		G.generate_rand_graph(40)
		dfs_marked = {}
		bfs_marked = {}
		explored = []
		start = G.rand_node()
		end = G.rand_node()
		dfs_t0 = time.time()
		dfs_dest(G, start, end, dfs_marked, explored)
		dfs_t1 = time.time()
		dfs_time += (dfs_t1 - dfs_t0)
		bfs_t0 = time.time()
		bfs_test = bfs_dest(G, start, end, bfs_marked)
		bfs_t1 = time.time()
		bfs_time += (bfs_t1 - bfs_t0)
		dfsm += len(dfs_marked)
		dfse += len(explored)
		bfsm += len(bfs_marked)
		try:
			bfse += len(bfs_test[1])
		except TypeError:
			bfse += 0
		dfsp = find_path(explored, start, end)
		dfspl += len(dfsp)
		try:
			bfsp = find_path(bfs_test[1], start, end)
		except TypeError:
			bfsp = False
		try:
			bfspl += len(bfsp)
		except TypeError:
			bfspl += 0
		print "\n---------------------"
		print "Test iter: %d" %(i + 1)
		print " Start: %s" %start
		print " End: %s" %end
		print " DFS marked: %d" %len(dfs_marked)
		print " BFS marked: %d" %len(bfs_marked)
		try:
			print " DFS path: %s" %format_path(dfsp)
		except IndexError:
			print " DFS path: No path"
		try:
			print " BFS path: %s" %format_path(bfsp)
		except TypeError:
			print " BFS path: No path"
	print "\n\n"
	print "Average DFS marked: %d" %(dfsm/test_iters)
	print "Average BFS marked: %d" %(bfsm/test_iters)
	print "Average DFS explored: %d" %(dfse/test_iters)
	print "Average BFS explored: %d" %(bfse/test_iters)
	print "Average DFS path length: %d" %(dfspl/test_iters)
	print "Average BFS path length: %d" %(bfspl/test_iters)
	print "DFS time/run: %.2f" %(dfs_time)
	print "BFS time/run: %.2f" %(bfs_time)
	print "BFS time / DFS time: %.2f" %(bfs_time / dfs_time)


def search_test(test_iters = 3):
	dfsm = 0
	bfsm = 0
	dfse = 0
	bfse = 0
	dfs_time = 0.0
	bfs_time = 0.0
	for i in range(test_iters):
		G = Graph()
		G.generate_rand_graph(40)
		dfs_marked = {}
		bfs_marked = {}
		explored = []
		start = G.rand_node()
		dfs_t0 = time.time()
		dfs(G, start, dfs_marked, explored)
		dfs_t1 = time.time()
		dfs_time += (dfs_t1 - dfs_t0)
		bfs_t0 = time.time()
		bfs_test = bfs(G, start, bfs_marked)
		bfs_t1 = time.time()
		bfs_time += (bfs_t1 - bfs_t0)
		dfsm += len(dfs_marked)
		dfse += len(explored)
		bfsm += len(bfs_marked)
		try:
			bfse += len(bfs_test[1])
		except TypeError:
			bfse += 0
		print "\n---------------------"
		print "Test iter: %d" %(i + 1)
		print " Nodes: %d" %len(G.nodes)
		print " Start: %s" %start
		print " DFS marked: %d" %len(dfs_marked)
		print " BFS marked: %d" %len(bfs_marked)
	print "\n\n"
	print "Average DFS marked: %d" %(dfsm/test_iters)
	print "Average BFS marked: %d" %(bfsm/test_iters)
	print "Average DFS explored: %d" %(dfse/test_iters)
	print "Average BFS explored: %d" %(bfse/test_iters)
	print "DFS time/run: %.2f" %(dfs_time)
	print "BFS time/run: %.2f" %(bfs_time)
	print "BFS time / DFS time: %.2f" %(bfs_time / dfs_time)

def big_search_test(test_iters = 100000):
	dfsm = 0
	bfsm = 0
	dfse = 0
	bfse = 0
	dfs_time = 0.0
	bfs_time = 0.0
	for i in range(test_iters):
		G = Graph()
		G.generate_rand_graph(40)
		dfs_marked = {}
		bfs_marked = {}
		explored = []
		start = G.rand_node()
		dfs_t0 = time.time()
		dfs(G, start, dfs_marked, explored)
		dfs_t1 = time.time()
		dfs_time += (dfs_t1 - dfs_t0)
		bfs_t0 = time.time()
		bfs_test = bfs(G, start, bfs_marked)
		bfs_t1 = time.time()
		bfs_time += (bfs_t1 - bfs_t0)
		dfsm += len(dfs_marked)
		dfse += len(explored)
		bfsm += len(bfs_marked)
		try:
			bfse += len(bfs_test[1])
		except TypeError:
			bfse += 0
		if i%1000 == 0:
			print i
	print "\n---------------------"
	print "Average DFS marked: %d" %(dfsm/test_iters)
	print "Average BFS marked: %d" %(bfsm/test_iters)
	print "Average DFS explored: %d" %(dfse/test_iters)
	print "Average BFS explored: %d" %(bfse/test_iters)
	print "DFS time/run: %.2f" %(dfs_time)
	print "BFS time/run: %.2f" %(bfs_time)
	print "BFS time / DFS time: %.2f" %(bfs_time / dfs_time)

def big_dest_test(test_iters = 100000):
	dfsm = 0
	bfsm = 0
	dfse = 0
	bfse = 0
	dfspl = 0
	bfspl = 0
	dfs_time = 0.0
	bfs_time = 0.0
	for i in range(test_iters):
		G = Graph()
		G.generate_rand_graph(40)
		dfs_marked = {}
		bfs_marked = {}
		explored = []
		start = G.rand_node()
		end = G.rand_node()
		dfs_t0 = time.time()
		dfs_dest(G, start, end, dfs_marked, explored)
		dfs_t1 = time.time()
		dfs_time += (dfs_t1 - dfs_t0)
		bfs_t0 = time.time()
		bfs_test = bfs_dest(G, start, end, bfs_marked)
		bfs_t1 = time.time()
		bfs_time += (bfs_t1 - bfs_t0)
		dfsm += len(dfs_marked)
		dfse += len(explored)
		bfsm += len(bfs_marked)
		try:
			bfse += len(bfs_test[1])
		except TypeError:
			bfse += 0
		dfsp = find_path(explored, start, end)
		dfspl += len(dfsp)
		try:
			bfsp = find_path(bfs_test[1], start, end)
		except TypeError:
			bfsp = False
		try:
			bfspl += len(bfsp)
		except TypeError:
			bfspl += 0
		if i%1000 == 0:
			print i
	print "\n---------------------"
	print "Average DFS marked: %d" %(dfsm/test_iters)
	print "Average BFS marked: %d" %(bfsm/test_iters)
	print "Average DFS explored: %d" %(dfse/test_iters)
	print "Average BFS explored: %d" %(bfse/test_iters)
	print "Average DFS path length: %d" %(dfspl/test_iters)
	print "Average BFS path length: %d" %(bfspl/test_iters)
	print "DFS time/run: %.2f" %(dfs_time)
	print "BFS time/run: %.2f" %(bfs_time)
	print "BFS time / DFS time: %.2f" %(bfs_time / dfs_time)