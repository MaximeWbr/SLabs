import requests
import csv

class DataBase():

	def __init__(self, name, listeURL, listeName):
		self.name = "name"
		self.listeDB = []
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

