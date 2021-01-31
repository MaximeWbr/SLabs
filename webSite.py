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

# #Crée une page user qui affiche le paramètre name
# @app.route("/<name>")
# def user(name):
# 	return f"hello {name}!"

# #Génère un simple plot
# @app.route("/generate")
# def generate():
# 	my_path = "../data/graphs/"+figPath 
# 	return	my_path
# 	#return redirect(url_for("plot", path=my_path))

# #Crée avec la page admin, redirige vers la page user avec comme input Admin!
# @app.route("/admin")
# def admin():
# 	return redirect(url_for("user", name="Admin!"))

@app.route('/plot', methods=['POST', 'GET'])
def image():
	if request.method == 'POST':
		result = request.form
		print(result)

	#CCreate folder for data base
	output_dir = TOULOUSE_PATH_DB
	mkdir_p(output_dir)
	# Get the corresponding data bases
	toulouseDB = DataBase("Toulouse", TOULOUSE_URL_LIST, TOULOUSE_NAME_LSIT)
	# Read the data bases
	toulouseDB._getData(output_dir+"Teso.csv")
	data = toulouseDB._getSpecificData("temperature_partie_decimale")
	# Plot data
	visu = Visualization()
	figName = visu._plotData("temperature_partie_decimale", data, 100)

	return render_template('plot.html', image_path =figName)

# #Crée une page et remplace content par name
# @app.route("/<name>")
# def home(name):
# 	#Affiche le fichier html
# 	return render_template("index.html", content=name)

if __name__ == "__main__":
	app.run()
















