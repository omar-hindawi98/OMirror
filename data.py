dataArray = {}

fileName = "/home/pi/Desktop/OMirror/settings/config.txt"

def readData():
    file = open(fileName, "r")
    
    for line in file:
        if line is not "":
            line = line.split("=")
            
            try:
                dataArray[line[0]] = line[1].replace("\n", "")
            except Exception:
                pass
    file.close()

def setData(key, value):
    try:
        dataArray[key] = value
        
        writeData()
        return 1
    except IndexError:
        return 0

def addNewData(key, value):
    dataArray[key] = value
    
    writeData()

def writeData():
    file = open(fileName, "w")
    
    for k, v in dataArray.items():
        string = "%s=%s\n" % (k, v)
        file.write(string)

    file.close()

def getData(key):
    return dataArray[key]