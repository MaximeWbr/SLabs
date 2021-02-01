from flask import Flask, redirect, url_for, request, render_template
from src.DataBase import *
from src.config import *
from src.Visualization import *
from src.mkdirPath import *
import matplotlib.pyplot as plt
import os


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

#Single Plot page
@app.route('/plot', methods=['POST', 'GET'])
def image():
	if request.method == 'POST':
		result = request.form
		city = request.form["city"]
		label = request.form["data"]
		s_number = int(request.form["sample_number"])

	# Create folder for data base
	output_dir = TOULOUSE_PATH_DB
	mkdir_p(output_dir)
	# Get the corresponding data bases
	toulouseDB = DataBase(city, TOULOUSE_URL_LIST, TOULOUSE_NAME_LSIT,0)
	# Read the data bases
	toulouseDB._getData(output_dir+"Teso.csv")
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
		

	# Create folder for data base
	output_dir = TOULOUSE_PATH_DB
	mkdir_p(output_dir)
	# Get the corresponding data bases
	toulouseDB = DataBase(city1, TOULOUSE_URL_LIST, TOULOUSE_NAME_LSIT,0)
	# Read the data bases
	toulouseDB._getData(output_dir+"Teso.csv")
	print(toulouseDB.listeLabel)
	data = toulouseDB._getSpecificData(label1)
	data2 = toulouseDB._getSpecificData(label2)
	# Plot data
	visu = Visualization()
	figName = visu._plotCompare(label1, data, label2, data2, s_number)
	return render_template('plotCompare.html', image_path =figName)

if __name__ == "__main__":
	app.run()
















