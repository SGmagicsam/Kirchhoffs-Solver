import numpy as np
from node import Node

class Circuit(object):

	def __init__(self):
		self._head = None

	def insert(self, item):
	
		new_node = Node(item)
		if not self._head:
			self._head = new_node


