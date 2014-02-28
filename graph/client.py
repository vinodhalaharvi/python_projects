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
from sets import Set
from Queue import Queue


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
	return 2.0 * G.numE() /G.numV(); 

def numberOfSelfLoops(G):
	"""docstring for numberOfSelfLoops"""
	count = 0 
	for v in range(G.numV()):
		for w in G.adj(v):
			if v == w:
				count += 1
	return count


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
        def E(self):
                """docstring for E"""
                for u in self.data.keys():
                        for v in self.data[u]:
                                yield u, v


        def V(self):
                """docstring for V"""
                for u in self.data.keys():
                        yield u

	def __iter__(self, ):
		for k, v in self.data.items():
			for v1 in v:
				yield k, v1
                              

	def numV(self,):
		"""docstring for numV"""
		return len(self.data.values())

	def numE(self):
		"""docstring for numE"""
		val = 0 
		for key in self.data.keys():
			val += len(self.data[key])
		return val

	def adj(self, v):
		return self.data[v]

	def xform(self, _from, to):
		"""docstring for xform"""
		return int(_from), int(to)

	def addEdge(self, _from, to):
		"""docstring for addEdge"""
		_from, to = self.xform(_from , to)
		if _from in self.data:
			#self.data[_from].append(to)
			self.data[_from].add(to)
		else:
			self.data[_from] = Set([to,])

	def print_graph(self):
		"""docstring for print_graph"""
		for edge in self.data.items():
			_from, to = edge
			print "%s->%s" % (_from, to)


class DFS(object):
        """docstring for Dfs"""
        def __init__(self, G, s):
                super(Dfs, self).__init__()
                self.G = G
                self.s = s


class Vertex(object):
        """docstring for Vertex"""
        def __init__(self, u):
                super(Vertex, self).__init__()
                self.u = u

        def __repr__(self):
                """docstring for __repr__"""
                return int(self.u)

        def __str__(self):
                """docstring for __str__"""
                return self.u


class BFS(object):
        """docstring for BFS"""
        def __init__(self):
                super(BFS, self).__init__()

        def bfs(G, s):
                setV = Set(G.V())
                for u in setV - Set(s):
                        u.color = WHITE
                        u.d = INF
                        u.pi = None
                s.color = GRAY
                s.d = 0 
                s.pi = None

                Q = Queue()
                Q.insert(s)
                while Q:
                        u = Q.remove()
                        for v in G.adj(u):
                                if v.color == WHITE:
                                        v.color = GRAY
                                        v.d = u.d + 1
                                        v.pi = u 
                                        Q.insert(v)
                        u.color = BLACK


if __name__ == '__main__':
	g = Graph(sys.stdin)
	g.print_graph()

        print 
        print "Edges are .." 
        for edge in  g.E():
                print edge
        print

        print "Vertices are .." 
        for v in  g.V():
                print v
        print


        '''
	print 
	for val in g:
		print val
	print
	print "maxDegree: %d" % maxDegree(g)
	print "degree of 1 is: %d" % degree(g, 1)
	print "averageDegree: %f" % averageDegree(g)
        print "Number of self loops: %d" % numberOfSelfLoops(g)
	print 
        '''
	
