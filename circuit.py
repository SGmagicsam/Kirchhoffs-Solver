import numpy as np
from node import Node

class Circuit(object):

	def __init__(self):
		
		self._size = 0
		#prev contains the tail and next contains the head
		self._sentinel_node = Node()

	def __iter__(self):
		'''
		Overriding the __iter__ function so I can traverse the circuit by saying "for node in circuit "etc
		'''
		current = self._sentinel_node.getNext()
		while(current != self._sentinel_node):
			yield current
			current = current.getNext()

	def insert(self, item):

		#if circuit is empty
		if not self._sentinel_node.getNext():
			new_node = Node(self._sentinel_node, self._sentinel_node, item)
			self._sentinel_node.setNext(new_node)
			self._sentinel_node.setPrev(new_node)
			return
		#otherwise
		new_node = Node(self._sentinel_node.getPrev(), self._sentinel_node, item)
		self._sentinel_node.getPrev().setNext(new_node)
		self._sentinel_node.setPrev(new_node)

	def printContent(self):

		for node in self:
			print(node.getData())



