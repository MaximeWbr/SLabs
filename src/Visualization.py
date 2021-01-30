import matplotlib.pyplot as plt
import numpy as np
from .mkdirPath import *
from .config import *

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
		#Crée le chemin
		output_dir = TOULOUSE_PATH_GRAPH 
		mkdir_p(output_dir)
		#Save the figure
		figureName = "{}/"+name+".png"
		plt.ylabel(name)
		plt.savefig(figureName.format(output_dir))
		#plt.show()

	# Description: Plot two datas to compare them on the same plot
	# Input: name1: (str) the first label name of the data
	#		 data1: (int list) the list of the first specific data
	#		 name2: (str) the second label name of the data
	#		 data2: (int list) the list of the second specific data
	#		 num:   (int) number of element to plot
	# Output: None
	def _plotCompare(self, name1, data1, name2, data2, num):
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
		#Crée le chemin
		output_dir = TOULOUSE_PATH_GRAPH 
		mkdir_p(output_dir)
		#Save the figure
		label = "{}/"+name1 + "_compare_to_" + name2
		figureName = label+".png"
		plt.suptitle(label)
		plt.savefig(figureName.format(output_dir))
		#plt.show()












