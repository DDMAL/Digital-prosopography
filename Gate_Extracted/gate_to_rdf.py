import os
import re
import xml.etree.ElementTree as ET
import sys

fileIn = "/Users/lhua/Documents/Digital-prosopography/Gate_Extracted/bakers_fixed/" + sys.argv[1]


tree = ET.parse(fileIn)
name = sys.argv[1].split('_')
first = name[0]
last = name[1]
root = tree.getroot()
fileOut = "/Users/lhua/Documents/Digital-prosopography/Gate_Extracted/rdf/" + first + "_" + last + ".np" 
f = open(fileOut, 'w+')
i = int(sys.argv[2])
Verb_pre = ""

def doNothing():
	""" we are really gonna do nothing here"""


for event in root.iter('event'):
	f.write("INSERT DATA { GRAPH <http://humanhistoryproject.ca/bakers> { <http://humanhistoryproject.ca/event_" + str(i) + "> <http://humanhistoryproject.ca/hasSubject> <http://humanhistoryproject.ca/" + first + "_" + last + "> }}")
	try:
		Verb = event.find('Verb').text
		if Verb != None:
			Verb_pre = Verb
		f.write('<http://humanhistoryproject.ca/event_' + str(i) + '> <http://humanhistoryproject.ca/hasAction> <http://humanhistoryproject.ca/' + Verb_pre + '> <http://humanhistoryproject.ca/Bakers> .') 
	except AttributeError, TypeError:
		doNothing()
	
	try:
		result = []
		for Object in event.findall('Object'):
			if Object.text != None:
				if Object.text != first or Object.text != last:
					result.append(Object.text)
			
		obj = result.join(" ")
		if obj != "":	
			f.write('<http://humanhistoryproject.ca/event_' + str(i) + '> <http://humanhistoryproject.ca/hasObject> <http://humanhistoryproject.ca/' + obj + '> <http://humanhistoryproject.ca/Bakers> .')
	
	except AttributeError, TypeError:
		doNothing()
	
	try:
		Location = event.find('Location').text
		if Location != None:	
			f.write('<http://humanhistoryproject.ca/event_' + str(i) + '> <http://humanhistoryproject.ca/hasLocation> <http://humanhistoryproject.ca/' + Location + '> <http://humanhistoryproject.ca/Bakers> .')
	
	except AttributeError, TypeError:
		doNothing()
	try:
		Date = event.find('Date').text
		if Date != None:		
			f.write('<http://humanhistoryproject.ca/event_' + str(i) + '> <http://humanhistoryproject.ca/hasTime> <http://humanhistoryproject.ca/' + Date + '> <http://humanhistoryproject.ca/Bakers> .')
	
	except AttributeError, TypeError:
		doNothing()


	i += 1
