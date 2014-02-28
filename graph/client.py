# Copyright (c) 2013, RTP Network Services, Inc.
# All Rights Reserved      (904-236-6993)
# Vinod Halaharvi / vinod.halaharvi@rtpnet.net, vinod.halaharvi@gmail.com
# 
# http://www.rtpnet.net / codesupport@rtpnet.net
#
# There is NO warranty for this software.  If this software is used by
# someone else and passed on, the recipients should know that what they
# have is not the original, so that any problems introduced by others will
# not reflect on the original authors' reputations. This is *not* authorization
# to copy or distribute this software to others!

import sys

def degree(G, v):
	"""docstring for adj"""
	return len(G.adj(v))

def maxDegree(G):
	"""docstring for maxDegree"""
	d = 0 
	max = 0 
	for v,e in G:
		d = degree(G,v)
		if max < d: 
			max = d
	return max

def averageDegree(G):
	"""docstring for averageDegree"""
	return 2.0 * G.E() /G.V(); 

def numberOfSelfLoops(G):
	"""docstring for numberOfSelfLoops"""
	count = 0 
	for v in range(G.V()):
		for w in G.adj(v):
			if v == w:
				count += 1
	return count/2


class Graph(object):
	"""docstring for Graph"""
	def __init__(self, arg):
		super(Graph, self).__init__()
		self.data = {}
		if isinstance(arg, int):
			self.vertices = range(arg)
		else:
			self.file = arg
			num_of_vertices = self.file.readline()
			num_of_edges = self.file.readline()
			for line in self.file.readlines():
				_from,to  = line.strip().split(" ", 2)
				self.addEdge(_from, to)

	def __iter__(self, ):
		for k, v in self.data.items():
			for v1 in v:
				yield k, v1

	def V(self,):
		"""docstring for V"""
		return len(self.data.values())

	def E(self):
		"""docstring for E"""
		val = 0 
		for key in self.data.keys():
			val += len(self.data[key])
		return val

	def adj(self, v):
		return self.data[v]

	def symbol(self, _from, to):
		"""docstring for symbol"""
		return int(_from), int(to)

	def addEdge(self, _from, to):
		"""docstring for addEdge"""
		_from, to = self.symbol(_from , to)
		if _from in self.data:
			self.data[_from].append(to)
		else:
			self.data[_from] = [to,]

	def print_graph(self):
		"""docstring for print_graph"""
		for edge in self.data.items():
			_from, to = edge
			print "%s->%s" % (_from, to)


class Paths(object):
	"""docstring for Paths"""
	def __init__(self, arg):
		super(Paths, self).__init__()
		pass

	def hasPathTo(self, v):
		"""docstring for hasPathTo(int v"""
		pass

	def pathTo(self, v):
		"""docstring for pathTo"""
		pass


class DepthFirstPaths(object):
	"""docstring for DepthFirstPaths"""
	def __init__(self, G, s):
		super(DepthFirstPaths, self).__init__()
		self.marked = {}
		for v in range(G.V()):
			self.marked[v] = False
		self.edgeTo = {}
		self._dfs(G, s)

	def _dfs(self, G, v):
		"""docstring for dfs"""
		self.marked[v] = True
		for w in G.adj(v): 
			if w in self.marked.keys() and not self.marked[w]:
				self._dfs(G, w)
				self.edgeTo[w] = v
	def print_dfs_state(self):
		"""docstring for print_dfs_state"""
		print self.marked
		print self.edgeTo


if __name__ == '__main__':
	g = Graph(sys.stdin)
	g.print_graph()
	print 
	for val in g:
		print val
	print
		
	print "maxDegree: %d" % maxDegree(g)
	print "degree: %d" % degree(g, 1)
	print "degree: %f" % averageDegree(g)
	print "Number of self loops %d:" % numberOfSelfLoops(g)
	print 
	DepthFirstPaths(g, 0).print_dfs_state()
	
