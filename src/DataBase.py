import requests
import csv

class DataBase():
	#Description: Constuctor
	# Input: url: (str) the url of the database for download
	#		pathName: (str) Path, name and extension to save data base
	#		flag: (int) 1 = download or update data base else no
	def __init__(self, url, pathName, flag):
		self.data = []
		self.listeName = pathName
		self.listeLabel = []
		#Download all the dataBase
		if(flag):
			r = requests.get(url, allow_redirects=True)
			open(pathName, 'wb').write(r.content)

	# Description: Get the data of the DB and save raw information into self.data (str list)
	# Input: pathName: (str) Path, name and extension to save data base
	# Output: None
	def _getData(self, pathName):
		data = []
		with open(pathName, 'r') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				data.append(row)
			self.listeLabel = data[0][0].split(";")
			for i in range(1, len(data)):
				self.data.append(data[i][0].split(";"))

	# Description: Get the data of the Air quality DB and save raw information into self.data (str list)
	# Input: pathName: (str) Path, name and extension to save data base
	# Output: None
	def _getDataAIR(self, pathName):
		data = []
		with open(pathName, 'r',encoding = "ISO-8859-1") as csvfile: #Change the encoding into "ISO-8859-1" for reading
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
	# Input: dataName: None
	# Output: sData: (int list 3D) the days, months and years available
	def _getDate(self):
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
	# Input: dataName: (str) the name of data label
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



