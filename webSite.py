from flask import Flask, redirect, url_for, request, render_template
from src.DataBase import *
from src.config import *
from src.Visualization import *
from src.mkdirPath import *
import matplotlib.pyplot as plt
import os

#Global Variable to allow the DB update
UPDATE_DB = 0

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#Main page 
@app.route("/", methods=['POST', 'GET'])
def home():
	return render_template('param.html')


@app.route("/paramSingle", methods=['POST', 'GET'])
def single():
	return render_template('paramSingle.html')

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

	if city == "Toulouse":
		output_dir = TOULOUSE_PATH_DB
		urlList = TOULOUSE_URL_LIST
		nameList = TOULOUSE_NAME_LSIT
	else:
		output_dir = AIR_PATH_DB
		urlList = AIR_URL
		nameList = AIR_NAME
	# Create folder for data base
	mkdir_p(output_dir)
	# Get the corresponding data bases
	toulouseDB = DataBase(city, urlList, nameList,UPDATE_DB)
	# Read the data bases
	toulouseDB._getData(nameList[0])
	data = toulouseDB._getSpecificData(label) #temperature_partie_decimale
	# Plot data
	visu = Visualization()
	figName = visu._plotData(label, data, s_number)
	return render_template('plot.html', image_path =figName)

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
		
	if city1 == "Toulouse":
		output_dir1 = TOULOUSE_PATH_DB
		urlList1 = TOULOUSE_URL_LIST
		nameList1 = TOULOUSE_NAME_LSIT
	else:
		output_dir1 = AIR_PATH_DB
		urlList1 = AIR_URL
		nameList1 = AIR_NAME

	if city2 == "Toulouse":
		output_dir2 = TOULOUSE_PATH_DB
		urlList2 = TOULOUSE_URL_LIST
		nameList2 = TOULOUSE_NAME_LSIT
	else:
		output_dir2 = AIR_PATH_DB
		urlList2 = AIR_URL
		nameList2 = AIR_NAME
	# Create folder for data base
	mkdir_p(output_dir1)
	mkdir_p(output_dir2)
	# Get the corresponding data bases
	dataBase1 = DataBase(city1, urlList1, nameList1, UPDATE_DB)
	dataBase2 = DataBase(city2, urlList2, nameList2, UPDATE_DB)
	# Read the data bases
	dataBase1._getData(nameList1[0])
	dataBase2._getData(nameList2[0])
	data = dataBase1._getSpecificData(label1)
	data2 = dataBase2._getSpecificData(label2)
	# Plot data
	visu = Visualization()
	figName = visu._plotCompare(label1, data, label2, data2, s_number)
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
		
	if city1 == "Toulouse":
		output_dir1 = TOULOUSE_PATH_DB
		urlList1 = TOULOUSE_URL_LIST
		nameList1 = TOULOUSE_NAME_LSIT
	else:
		output_dir1 = AIR_PATH_DB
		urlList1 = AIR_URL
		nameList1 = AIR_NAME

	output_dir2 = AIR_PATH_DB
	urlList2 = AIR_URL
	nameList2 = AIR_NAME
	# Create folder for data base
	mkdir_p(output_dir1)
	mkdir_p(output_dir2)
	# Get the corresponding data bases
	dataBase1 = DataBase(city1, urlList1, nameList1, UPDATE_DB)
	dataBase2 = DataBase(city2, urlList2, nameList2, UPDATE_DB)
	# Read the data bases
	dataBase1._getData(nameList1[0])
	dataBase2._getDataAIR(nameList2[0])
	data = dataBase1._getSpecificData(label1)
	data2 = dataBase2._getSpecificData(label2)
	# Plot data
	visu = Visualization()
	figName = visu._plotCompare(label1, data, label2, data2, s_number)
	return render_template('plotCompare.html', image_path =figName)

if __name__ == "__main__":
	app.run()
















