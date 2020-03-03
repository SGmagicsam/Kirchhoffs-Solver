import numpy as np

class Node(object):
	def __init__(self, data):
		self._data = data
		self._adjacent_nodes = np.array()