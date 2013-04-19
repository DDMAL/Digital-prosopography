import os
import re

#fileOut = raw_input('Type in the Name of the output file: ')
fileList = os.listdir("entire")

for inFile in fileList:
	fileOut = "entireXML/"+inFile

	rFile = open(fileOut,'wb')
	rFile.write('<?xml version="1.0" encoding="UTF-8"?>')
	rFile.write("<Data>")
	oFile = open("entire/"+inFile, "r")
	text = oFile.read()
	#re.sub('<[^<]+?>', '', text)

	rFile.write(text)
	rFile.write("</Data>")
	print inFile+" Done.\n"
	rFile.close()
	oFile.close()

#wr = csv.writer(resultFile, dialect='excel')

#fileIn = raw_input('Type in the Name of the input file: ')
#fileIn = "Names1.xml"


#tree = ET.parse(fileIn)
#root = tree.getroot()

#for Sentence in root.iter('Person'):
#    S = Sentence.text
 #   if S != None:
       
#        wr.writerow(S)
 
#        print S
#    else:
#        print "None"



#resultFile.close()