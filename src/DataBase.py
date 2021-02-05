import requests
import csv

class DataBase():

	def __init__(self, name, listeURL, listeName, flag):
		self.data = []
		self.listeName = listeName
		self.listeLabel = []
		#Download all the dataBase
		if(flag):
			#for i in range(0, len(listeURL)):
			url = listeURL#[i]
			r = requests.get(url, allow_redirects=True)
			open(listeName, 'wb').write(r.content)

	# Description: Get the data of the DB and save raw information into self.data (str list)
	# Input: name: (str) the name of the data base
	# Output: None
	def _getData(self, name):
		data = []
		#index = self.listeName.index(name)
		with open(name, 'r') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				data.append(row)
			self.listeLabel = data[0][0].split(";")
			for i in range(1, len(data)):
				self.data.append(data[i][0].split(";"))

	# Description: Get the data of the DB and save raw information into self.data (str list)
	# Input: name: (str) the name of the data base
	# Output: None
	def _getDataAIR(self, name):
		data = []
		#index = self.listeName.index(name)
		with open(name, 'r',encoding = "ISO-8859-1") as csvfile: #Change the encoding into "ISO-8859-1" for reading
			reader = csv.reader(csvfile)
			for row in reader:
				data.append(row)
			self.listeLabel = data[0][0].split(";")
			for i in range(1, len(data)):
				self.data.append(data[i][0].split(";"))
	
	# Description: Get the data of a specific label
	# Input: dataName: (str) the name of data label
	# Output: sData: (int list) the data of the asked label 
	def _getSpecificData(self, dataName):
		sData = []
		index = self.listeLabel.index(dataName)
		for i in range(0, len(self.data)):
			val = self.data[i][index].split(".")
			sData.append(int(val[0]))
		return sData

	# Description: Get the date available in the DB
	# Input: dataName: (str) the name of data base
	# Output: sData: (int list 3D) the days, months and years available
	def _getDate(self, nameDB):
		date = [[],[],[]]
		label = ["mois","annee"]
		for j in range(0, len(label)):
			tmp = []
			index = self.listeLabel.index(label[j])
			for i in range(0, len(self.data)):
				val = self.data[i][index].split(".")
				tmp.append(int(val[0]))
			tmp = list(set(tmp))
			date[j] = tmp
		return date

	# Description: Get the data in function of a date
	# Input: dataName: (str) the name of data base
	#					(str) the selected day
	#					(str) the selected month
	#					(str) the selected year
	# Output: sData: (int list) the data of the asked label 
	def _getDateData(self, dataName, month, year):
		sData = []
		index = self.listeLabel.index(dataName)
		index_month = self.listeLabel.index("mois")
		index_year = self.listeLabel.index("annee")
		for i in range(0, len(self.data)):
			if self.data[i][index_month] == month and self.data[i][index_year] == year:
				val = self.data[i][index].split(".")
				sData.append(int(val[0]))
		return sData



