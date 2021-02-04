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
		#Safety take the max of available data
		if len(data)<num:
			num = len(data)
		#Get the num last values of data
		for i in range(num):
			tmpData.append(data[num-(i+1)])
		#Scale x
		x = np.linspace(1,num,num)
		plt.switch_backend('Agg') #matplotlib set the backend to a non-interactive one in order to the server does not try to create (and then destroy) GUI windows that will never be seen.
		plt.plot(x,tmpData)
		plt.suptitle("Representation of the '"+ name +"' for the "+ str(num) +" last times")
		plt.ylabel(name)
		plt.xlabel("The "+ str(num) + " last data received")
		plt.savefig(figureName)
		return name+".png"

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
		#Safety take the max of available data
		if len(data1)<num:
			num = len(data1)
		if len(data2)<num:
			num = len(data2)
		#Get the num last values of the data1 and data2
		for i in range(num):
			tmpData1.append(data1[num-(i+1)])
			tmpData2.append(data2[num-(i+1)])
		if max(tmpData1) != 0:
			normData1 = [float(i)/max(tmpData1) for i in tmpData1]
		else:
			normData1 = tmpData1
		if max(tmpData2) != 0:
			normData2 = [float(j)/max(tmpData2) for j in tmpData2]
		else:
			normData2 = tmpData2
		#Scale x1 and x2
		x1 = np.linspace(1,num,num)
		x2 = np.linspace(1,num,num)
		plt.switch_backend('Agg') #matplotlib set the backend to a non-interactive one in order to the server does not try to create (and then destroy) GUI windows that will never be seen.
		plt.plot(x1, normData1, 'b', x2, normData2, 'r')
		#Create path for figure
		output_dir = TOULOUSE_PATH_GRAPH 
		mkdir_p(output_dir)
		#Save the figure
		label =name1 + "_compare_to_" + name2
		figureName = output_dir+label+".png"
		if name2 == "valeur":
			plotName = "Air Quality"
		else:
			plotName = name2
		plt.suptitle("Compare '"+ name1 +"' to '"+ plotName +"' for the "+ str(num) +" last times")
		plt.ylabel("Normalized data")
		plt.xlabel("The "+ str(num) +" last data received")
		plt.legend((name1, plotName), loc='upper right')
		plt.savefig(figureName)
		return name1 + "_compare_to_" + name2 +".png"













