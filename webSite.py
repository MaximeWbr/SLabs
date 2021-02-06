from flask import Flask, redirect, url_for, request, render_template
from src.DataBase import *
from src.config import *
from src.Visualization import *
from src.mkdirPath import *
import matplotlib.pyplot as plt
import os
from datetime import timedelta

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#Main page 
@app.route("/", methods=['POST', 'GET'])
def home():
	return render_template('param.html')


@app.route("/paramSingle", methods=['POST', 'GET'])
def single():
	return render_template('paramSingle.html')

@app.route("/paramSingleDate", methods=['POST', 'GET'])
def singleDate():
	return render_template('paramSingleDate.html')

@app.route("/paramCompare", methods=['POST', 'GET'])
def Compare():
	return render_template('paramCompare.html')

@app.route("/paramCompareAirQuality", methods=['POST', 'GET'])
def AirCompare():
	return render_template('paramCompareAirQuality.html')

#Single Plot page
@app.route('/plot', methods=['POST', 'GET'])
def image():
	if request.method == 'POST':
		result = request.form
		city = request.form["city"]
		label = request.form["data"]
		s_number = int(request.form["sample_number"])

	# Check the value of sample number
	if s_number < 0:
		return render_template('paramSingleAlerte.html')
	#Replace "temperature_partie_decimale" by "temperature" because doesn't have the same label name
	if(city == "Toulouse_La_Salade" and label == "temperature_partie_entiere"):
		label ="temperature_en_degre_c"

	nameIndex = NAME_INDEX.index(city)
	output_dir = TOULOUSE_PATH_DB
	urlList = TOULOUSE_URL_LIST[nameIndex]
	nameList = TOULOUSE_NAME_LSIT[nameIndex]

	# Create folder for data base
	mkdir_p(output_dir)
	# Check time to download the new DB or not, update every 15min (Weather DB)
	yearTime = timedelta(days=365)
	yearTime.total_seconds()
	global TIME
	if (yearTime.total_seconds() < TIME[nameIndex]+(15*60)):
		UPDATE_DB = 0
	else:
		UPDATE_DB = 1
		TIME[nameIndex] = yearTime.total_seconds()
	# Get the corresponding data bases
	toulouseDB = DataBase(city, urlList, nameList,UPDATE_DB)
	# Read the data bases
	toulouseDB._getData(nameList)
	data = toulouseDB._getSpecificData(label) #temperature_partie_decimale
	# Plot data
	visu = Visualization()
	figName = visu._plotData(label, data, s_number)
	return render_template('plot.html', image_path =figName)

#Single Plot page
@app.route('/plotDate', methods=['POST', 'GET'])
def imageDate():
	if request.method == 'POST':
		result = request.form
		city = request.form["city"]
		label = request.form["data"]
		month = request.form["month"]
		year = request.form["year"]
		s_number = int(request.form["sample_number"])

	# Check the value of sample number
	if s_number < 0:
		return render_template('paramSingleDateAlerteSample.html')
	#Replace "temperature_partie_decimale" by "temperature" because doesn't have the same label name
	if(city == "Toulouse_La_Salade" and label == "temperature_partie_entiere"):
		label ="temperature_en_degre_c"

	nameIndex = NAME_INDEX.index(city)
	output_dir = TOULOUSE_PATH_DB
	urlList = TOULOUSE_URL_LIST[nameIndex]
	nameList = TOULOUSE_NAME_LSIT[nameIndex]

	# Create folder for data base
	mkdir_p(output_dir)
	# Check time to download the new DB or not, update every 15min (Weather DB)
	yearTime = timedelta(days=365)
	yearTime.total_seconds()
	global TIME
	if (yearTime.total_seconds() < TIME[nameIndex]+(15*60)):
		UPDATE_DB = 0
	else:
		UPDATE_DB = 1
		TIME[nameIndex] = yearTime.total_seconds()
	# Get the corresponding data bases
	toulouseDB = DataBase(city, urlList, nameList,UPDATE_DB)
	# Read the data bases
	toulouseDB._getData(nameList)
	data = toulouseDB._getDateData(label, month, year)
	if len(data) == 0:
		return render_template('paramSingleDateAlerte.html')
	toulouseDB._getDate(city)
	# Plot data
	visu = Visualization()
	figName = visu._plotData(label, data, s_number)
	return render_template('plotDate.html', image_path =figName)

#Compare Plot page
@app.route('/plotCompare', methods=['POST', 'GET'])
def imageCompare():
	if request.method == 'POST':
		result = request.form
		city1 = request.form["city"]
		label1 = request.form["data"]
		s_number = int(request.form["sample_number"])
		city2 = request.form["city2"]
		label2 = request.form["data2"]

	# Check the value of sample number
	if s_number < 0:
		return render_template('paramCompareAlerte.html')
	#Replace "temperature_partie_decimale" by "temperature" because doesn't have the same label name
	if(city1 == "Toulouse_La_Salade" and label1 == "temperature_partie_entiere"):
		label1 ="temperature_en_degre_c"
	if(city2 == "Toulouse_La_Salade" and label2 == "temperature_partie_entiere"):
		label2 ="temperature_en_degre_c"

	nameIndex = NAME_INDEX.index(city1)
	output_dir1 = TOULOUSE_PATH_DB
	urlList1 = TOULOUSE_URL_LIST[nameIndex]
	nameList1 = TOULOUSE_NAME_LSIT[nameIndex]

	nameIndex2 = NAME_INDEX.index(city2)
	output_dir2 = TOULOUSE_PATH_DB
	urlList2 = TOULOUSE_URL_LIST[nameIndex]
	nameList2 = TOULOUSE_NAME_LSIT[nameIndex]

	# Create folder for data base
	mkdir_p(output_dir1)
	mkdir_p(output_dir2)
	# Check time to download the new DB or not, update every 15min (Weather DB)
	yearTime = timedelta(days=365)
	yearTime.total_seconds()
	global TIME
	if (yearTime.total_seconds() < TIME[nameIndex]+(15*60)):
		UPDATE_DB = 0
	else:
		UPDATE_DB = 1
		TIME[nameIndex] = yearTime.total_seconds()
	# Get the corresponding data bases
	dataBase1 = DataBase(city1, urlList1, nameList1, UPDATE_DB)
	dataBase2 = DataBase(city2, urlList2, nameList2, UPDATE_DB)
	# Read the data bases
	dataBase1._getData(nameList1)
	dataBase2._getData(nameList2)
	data = dataBase1._getSpecificData(label1)
	data2 = dataBase2._getSpecificData(label2)
	# Plot data
	visu = Visualization()
	figName = visu._plotCompare(label1, data, label2, data2, s_number, city1, city2)
	return render_template('plotCompare.html', image_path =figName)

#The weather data and air quality compare page
@app.route('/plotCompareAirQuality', methods=['POST', 'GET'])
def imageAirCompare():
	if request.method == 'POST':
		result = request.form
		city1 = request.form["city"]
		label1 = request.form["data"]
		s_number = int(request.form["sample_number"])
		city2 = request.form["city2"]
		label2 = "valeur"

	# Check the value of sample number
	if s_number < 0:
		return render_template('paramCompareAirQualityAlerte.html')
	#Replace "temperature_partie_decimale" by "temperature" because doesn't have the same label name
	if(city1 == "Toulouse_La_Salade" and label1 == "temperature_partie_entiere"):
		label1 ="temperature_en_degre_c"

	nameIndex = NAME_INDEX.index(city1)
	output_dir1 = TOULOUSE_PATH_DB
	urlList1 = TOULOUSE_URL_LIST[nameIndex]
	nameList1 = TOULOUSE_NAME_LSIT[nameIndex]

	output_dir2 = AIR_PATH_DB
	urlList2 = AIR_URL
	nameList2 = AIR_NAME

	# Create folder for data base
	mkdir_p(output_dir1)
	mkdir_p(output_dir2)
	# Check time to download the new DB or not, update every 9min (Air Quality BD)
	yearTime = timedelta(days=365)
	yearTime.total_seconds()
	global TIME_AIR
	global TIME
	if ((yearTime.total_seconds() < TIME_AIR+(9*60)) or (yearTime.total_seconds() < TIME[nameIndex]+(15*60))):
		UPDATE_DB = 0
	else:
		UPDATE_DB = 1
		TIME_AIR = yearTime.total_seconds()
		TIME[nameIndex] = yearTime.total_seconds()
	# Get the corresponding data bases
	dataBase1 = DataBase(city1, urlList1, nameList1, UPDATE_DB)
	dataBase2 = DataBase(city2, urlList2, nameList2, UPDATE_DB)
	# Read the data bases
	dataBase1._getData(nameList1)
	dataBase2._getDataAIR(nameList2)
	data = dataBase1._getSpecificData(label1)
	data2 = dataBase2._getSpecificData(label2)
	# Plot data
	visu = Visualization()
	figName = visu._plotCompare(label1, data, label2, data2, s_number, city1, city2)
	return render_template('plotCompare.html', image_path =figName)

if __name__ == "__main__":
	app.run()
















