import matplotlib.pyplot as plt
import numpy as np
from .mkdirPath import *
from .config import *

class Visualization():

	# Description: Plot one data
	# Input: name: (str) the label name of the data
	#		 data: (int list) the list of the specific data
	#		 num:  (int) number of element to plot
	# Output: (str) the name of the figure
	def _plotData(self, name, data, num):
		#Create path for figure
		output_dir = TOULOUSE_PATH_GRAPH 
		mkdir_p(output_dir)
		#Save the figure
		figureName = output_dir+name+".png"
		tmpData = []
		#Get the num last values of data
		for i in range(num):
			tmpData.append(data[num-(i+1)])
		#Scale x
		x = np.linspace(min(tmpData),max(tmpData),len(tmpData))
		plt.switch_backend('Agg') #matplotlib set the backend to a non-interactive one in order to the server does not try to create (and then destroy) GUI windows that will never be seen.
		plt.plot(x,tmpData)

		plt.ylabel(name)
		plt.savefig(figureName)
		return name+".png"
		#plt.show()

	# Description: Plot two datas to compare them on the same plot
	# Input: name1: (str) the first label name of the data
	#		 data1: (int list) the list of the first specific data
	#		 name2: (str) the second label name of the data
	#		 data2: (int list) the list of the second specific data
	#		 num:   (int) number of element to plot
	# Output: (str) the name of the figure
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
		return name1 + "_compare_to_" + name2
		#plt.show()












