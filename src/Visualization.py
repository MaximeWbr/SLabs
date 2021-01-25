import matplotlib.pyplot as plt

class Visualization():

	def _plotData(self, name, data):
		plt.plot(data)
		plt.ylabel(name)
		plt.show()

	def _plotCompare(self, name1, data1, name2, data2):
		plt.plot(data1, 'b', data2, 'r')
		label = name1 + " compare to " + name2
		plt.suptitle(label)
		plt.show()