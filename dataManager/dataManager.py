import os
import time

# <------------------------ Main Function ----------------------->

def main():
	
	confPath = "~/" #absolute path for device configuration file

	#devices = loadConf(confPath)
	devices = ["MQ9"]

	try:
		while 1:
			time.sleep(5)
			for dev in devices:
				tempFilePath = "Temp/" + dev + "_" + "1"
				data = loadTempFile(tempFilePath)

				deleteTempFile(tempFilePath)

				permFilePath = "Storage/" + dev
				savePermFile(permFilePath, data)
	except Keyboardinterrupt:
		print "Exit program"



#-------------
# def test1():
# 	# with open("Incoming/MGodfrey.csv") as f:
# 	# 	# content = f.readline()
# 	# 	content = f.read()
# 	# 	print content

# 	# f.close()

# 	output =  open("Storage/output.csv", "w+")
# 	# output =  open("Storage/output.csv", "a+") "a+" for appending the file, 
#   not overwriting.
# 	output.write(content)

# 	output.close()

def createJSON():

	dictlist={}

	with open("../client/ui/media/data/example") as file1:	
		for line in file1:
			temp=line.split()
			if temp!=[]:
				dictlist["t"+"".join(temp[0].split("/"))+"".join(temp[1].split\
					(":"))]=temp[3]

	file1.close()

	with open("../client/ui/media/data/testoutput.json", "w") as outfile:
		json.dump(dictlist, outfile)

# createJSON()

# <---------------------------------- Helper functions ----------------------->

def loadConf(filepath):
	'''Given filepath of device configuration file absolute path, return a list
	of device names '''

	devices = []
	with open(filepath) as configFile:
		for line in configFile:
			tempstring = line.strip()
			if tempstring != "":
				devices.append(tempstring)
	configFile.close()

	return devices


def loadTempFile(filepath):
	'''Take filepath to load temp data files from the sensors and return the 
	sensor data in a variable'''

	data = ""

	if os.path.exists(filepath):

		with open(filepath) as tempFile:
			data = tempFile.read()

		tempFile.close()

	return data

def deleteTempFile(filepath):
	'''Given filepath, delete target temp file of sensor data after reading
	them'''

	if os.path.exists(filepath):
		os.remove(filepath)

def savePermFile(filepath, data):
	'''Given a filepath and data variable, save the data into the target file
	with name. If the file is already there, append data at the end of it'''

	if os.path.exists(filepath):
		with open(filepath, "a+") as f:
			f.write(data)
	else:
		with open(filepath, "w+") as f:
			f.write(data)
	
	f.close()


# Executing code:

if __name__=="__main__":

	main()
