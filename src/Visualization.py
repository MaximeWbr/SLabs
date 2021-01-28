import matplotlib.pyplot as plt
import numpy as np

class Visualization():

	# Description: Plot one data
	# Input: name: (str) the label name of the data
	#		 data: (int list) the list of the specific data
	#		 num:  (int) number of element to plot
	# Output: None
	def _plotData(self, name, data, num):
		tmpData = []
		#Get the num last values of data
		for i in range(num):
			tmpData.append(data[num-(i+1)])
		#Scale x
		x = np.linspace(min(tmpData),max(tmpData),len(tmpData))
		plt.plot(x,tmpData)
		plt.ylabel(name)
		plt.show()

	# Description: Plot two datas to compare them on the same plot
	# Input: name:  (str) the first label name of the data
	#		 data1: (int list) the list of the first specific data
	#		 data2: (int list) the list of the second specific data
	#		 num:   (int) number of element to plot
	# Output: None
	def _plotCompare(self, name, data1, data2, num):
		tmpData1 = []
		tmpData2 = []
		#Get the num last values of the data1 and data2
		for i in range(num):
			tmpData1.append(data1[num-(i+1)])
			tmpData2.append(data2[num-(i+1)])
		#Scale x1 and x2
		x1 = np.linspace(min(tmpData1),max(tmpData1),len(tmpData1))
		x2 = np.linspace(min(tmpData2),max(tmpData2),len(tmpData2))
		plt.plot(x1, tmpData1, 'b', x2, tmpData2, 'r')
		label = name + " compare to " + name
		plt.suptitle(label)
		plt.show()