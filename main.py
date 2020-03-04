from circuit import Circuit
from battery import Battery
from node import Node

def main():


	circuit = Circuit()
	battery = Battery(15)
	circuit.insert(battery)
	circuit.printContent()
if __name__ == "__main__":
	main()
