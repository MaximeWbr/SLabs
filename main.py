from src.DataBase import *
from src.config import *
#List of URL for the city

print("Welcome, Choose your city:\n(1) Toulouse\n")
choise = input('Enter your answer: ')
if choise == "1" or choise == "Toulouse":
	print("You have chosen Toulouse.\n")
	# Get the corresponding data bases
	toulouseDB = DataBase("Toulouse", TOULOUSE_URL_LIST, TOULOUSE_NAME_LSIT)
	# Read the data bases
	# Generate the website
		# Once created ask to visit it
	# Show on the website
		# City's data
		# Ask for action (compare with Air Quality, Update)
else:
	print("Error: Wrong answer, code exit.")

	# For more Cities
		# Create a SQL data set to save D.B (Key = city name)