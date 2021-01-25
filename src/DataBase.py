import requests
import csv

class DataBase():

	def __init__(self, name, listeURL, listeName):
		self.name = "name"
		self.listeDB = []
		self.listeName = listeName
		self.listeLabel = []
		#Download all the dataBase
		for i in range(0, len(listeURL)):
			# Get the file and save it in data folder
			url = listeURL[i]
			r = requests.get(url, allow_redirects=True)
			open(listeName[i], 'wb').write(r.content)
			# Read the data set and save it in the dataBase list
			with open(listeName[i], newline='') as csvfile:
				mydata = csv.DictReader(csvfile)
				self.listeDB.append(mydata)

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
			self.listeLabel = data[0]
			return data



