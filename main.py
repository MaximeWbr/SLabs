from src.DataBase import *
from src.config import *
from src.Visualization import *
from src.mkdirPath import *

print("Welcome, Choose your city:\n(1) Toulouse\n")
choise = input('Enter your answer: ')
if choise == "1" or choise == "Toulouse":
	print("You have chosen Toulouse.\n")

	#Create the Data Base container folder
	output_dir = TOULOUSE_PATH_DB
	mkdir_p(output_dir)

	# Get the corresponding data bases
	toulouseDB = DataBase("Toulouse", TOULOUSE_URL_LIST, TOULOUSE_NAME_LSIT,0)
	# Read the data bases
	toulouseDB._getData(output_dir+"Teso.csv")
	data = toulouseDB._getSpecificData("temperature_partie_decimale")

	#Website
		# Once created ask to visit it
	# Show on the website
		# City's data
			#Plot data
	visu = Visualization()
	name1 = visu._plotData("temperature_partie_decimale", data, 20)
	name2 = visu._plotCompare("temperature_partie_decimale", data, "temperature_partie_decimale", data, 20)

		# Ask for action (compare with Air Quality, Update)
else:
	print("Error: Wrong answer, code exit.")

	# For more Cities
		# Create a SQL data set to save D.B (Key = city name)