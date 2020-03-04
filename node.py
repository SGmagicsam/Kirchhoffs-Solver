import numpy as np

class Node(object):

	def __init__(self, prev = None, next = None, data = None):

		self._prev = prev
		self._next = next
		self._data = data
		self._adjacent_nodes = np.array([])

	def connect(self, node):

		np.insert(self._adjacent_nodes, node)

	def getData(self):
		return self._data
	def getPrev(self):
		return self._prev
	def getNext(self):
		return self._next
	def setPrev(self, node):
		self._prev = node
	def setNext(self, node):
		self._next = node
