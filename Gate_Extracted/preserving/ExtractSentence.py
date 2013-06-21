import os.path

import xml.etree.ElementTree as ET

fileOut = "Bakers.xml"

resultFile = open(fileOut,'wb')


fileIn = "BakersBornandDeath.xml"

tree = ET.parse(fileIn)
root = tree.getroot()

for item in root.iter():
    resultFile.write(item)

resultFile.close()