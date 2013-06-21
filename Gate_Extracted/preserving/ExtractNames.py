import os
import re
import xml.etree.ElementTree as ET

#fileOut = raw_input('Type in the Name of the output file: ')
"""fileList = os.listdir("entire")

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

#wr = csv.writer(resultFile, dialect='excel')"""

#fileIn = raw_input('Type in the Name of the input file: ')
fileIn = "Aaron_suggested.xml"

tree = ET.parse(fileIn)
root = tree.getroot()
i = 1
for event in root.iter('event'):
	#print "INSERT DATA { GRAPH <http://humanhistoryproject.ca/source10001> { <http://humanhistoryproject.ca/event_" + str(i) + "> <http://humanhistoryproject.ca/hasSubject> <http://humanhistoryproject.ca/Aaron_Pietro> }}"
	#print '<http://humanhistoryproject.ca/event_' + str(i) + '>'
	try:
		Verb = event.find('Verb').text
		if Verb != None:
			#print "INSERT DATA { GRAPH <http://humanhistoryproject.ca/source10001> { <http://humanhistoryproject.ca/event_" + str(i) + "> <http://humanhistoryproject.ca/hasAction> <http://humanhistoryproject.ca/" + Verb + "> }}"
			print '<http://humanhistoryproject.ca/event_' + str(i) + '> <http://humanhistoryproject.ca/hasAction> <http://humanhistoryproject.ca/' + Verb + '> <http://humanhistoryproject.ca/Bakers> .'
	except AttributeError, TypeError:
		print " "
	try:
		Object = event.find('Object').text
		if Object != None:
			#print "INSERT DATA { GRAPH <http://humanhistoryproject.ca/source10001> { <http://humanhistoryproject.ca/event_" + str(i) + "> <http://humanhistoryproject.ca/hasObject> <http://humanhistoryproject.ca/" + Object + "> }}"
			print '<http://humanhistoryproject.ca/event_' + str(i) + '> <http://humanhistoryproject.ca/hasObject> <http://humanhistoryproject.ca/' + Object + '> <http://humanhistoryproject.ca/Bakers> .'
	
	except AttributeError, TypeError:
		print " "
	try:
		Location = event.find('Location').text
		if Location != None:
			#print "INSERT DATA { GRAPH <http://humanhistoryproject.ca/source10001> { <http://humanhistoryproject.ca/event_" + str(i) + "> <http://humanhistoryproject.ca/hasLocation> <http://humanhistoryproject.ca/" + Location + "> }}"
			print '<http://humanhistoryproject.ca/event_' + str(i) + '> <http://humanhistoryproject.ca/hasLocation> <http://humanhistoryproject.ca/' + Location + '> <http://humanhistoryproject.ca/Bakers> .'
	
	except AttributeError, TypeError:
		print " "
	try:
		Date = event.find('Date').text
		if Date != None:
			#print "INSERT DATA { GRAPH <http://humanhistoryproject.ca/source10001> { <http://humanhistoryproject.ca/event_" + str(i) + "> <http://humanhistoryproject.ca/hasTime> <http://humanhistoryproject.ca/" + Date + "> }}"
			print '<http://humanhistoryproject.ca/event_' + str(i) + '> <http://humanhistoryproject.ca/hasTime> <http://humanhistoryproject.ca/' + Date + '> <http://humanhistoryproject.ca/Bakers> .'
	
	except AttributeError, TypeError:
		print " "


	i += 1