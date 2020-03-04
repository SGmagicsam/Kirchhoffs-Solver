import numpy as np

class Battery(object):

	def __init__(self, emf):
		self._emf = emf

	def __repr__(self):
		return f"{self._emf}V Battery"

	def getVoltage(self):
		return self._emf

	def setVoltage(self, voltage):
		self._emf = voltage

