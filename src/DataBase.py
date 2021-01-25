import requests
import csv

class DataBase():

	def __init__(self, name, listeURL, listeName):
		self.name = "name"
		self.data = []
		self.listeName = listeName
		self.listeLabel = []
		#Download all the dataBase
		#for i in range(0, len(listeURL)):
		#	# Get the file and save it in data folder
		#	url = listeURL[i]
		#	r = requests.get(url, allow_redirects=True)
		#	open(listeName[i], 'wb').write(r.content)

	# Description: Get the data of the DB
	# Input: (str) the name of the data base
	# Output: (list) the contain of the data, each line is a day and each column is a data type 
	def _getData(self, name):
		data = []
		index = self.listeName.index(name)
		with open(self.listeName[index], 'r') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				data.append(row)
			self.listeLabel = data[0][0].split(";")
			for i in range(1, len(data)):
				self.data.append(data[i][0].split(";"))

	def _getSpecificData(self, dataName):
		sData = []
		index = self.listeLabel.index(dataName)
		for i in range(0, len(self.data)):
			sData.append(self.data[i][index])
		print(sData)
		return sData



