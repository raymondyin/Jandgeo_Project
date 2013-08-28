import nose
from dataManager import loadConf

def testLoadConfig():
	path = "Config/Devices.txt"
	lst = loadConf(path)
	assert len(lst) == 4
	assert lst == ["MQ9","MQ5","MQ3","MQ2"]

if __name__ == '__main__':
	nose.main()