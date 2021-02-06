#URL of the data base for doxnload and update
TOULOUSE_URL_LIST = ["https://www.data.gouv.fr/fr/datasets/r/264fe552-4f8a-4253-8afb-f0df65025fbf",
					"https://www.data.gouv.fr/fr/datasets/r/8b5d53af-011f-4518-b12c-54b3030db412",
					"https://www.data.gouv.fr/fr/datasets/r/47f72f21-eba6-4620-810d-ebd3c228aaf0"]

AIR_URL = "https://www.arcgis.com/sharing/rest/content/items/59b95f2f49c948519ebf58bc058ec7e2/data"

#Path to store data base
TOULOUSE_PATH_DB = "./data/Toulouse/"
AIR_PATH_DB = "./data/"
TOULOUSE_PATH_GRAPH = "static/images/"

#Path, name and extension to save data base
TOULOUSE_NAME_LIST= ["./data/Toulouse/Teso.csv","./data/Toulouse/George_Sand.csv", "./data/Toulouse/La_Salade.csv"]
AIR_NAME= "./data/AirQuality.csv"

#Name of the download data base
NAME_INDEX =["Toulouse_Tesco","Toulouse_George_Sand", "Toulouse_La_Salade"]

#Global Variable to allow the DB update
UPDATE_DB = 0
TIME = [0,0,0]
TIME_AIR = 0