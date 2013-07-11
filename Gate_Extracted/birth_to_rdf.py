import os
import re
import xml.etree.ElementTree as ET
import sys
from time import gmtime, strftime

fileIn = "/Users/lhua/Documents/Digital-prosopography/Gate_Extracted/bakers_extracted/" + sys.argv[1]


tree = ET.parse(fileIn)
name = sys.argv[1].split('.')
first_last = name[0]
root = tree.getroot()
fileOut = "/Users/lhua/Documents/Digital-prosopography/Gate_Extracted/rdf/" + first_last + ".nq" 
f = open(fileOut, 'w+')
i = int(sys.argv[2])
Verb_pre = ""

def doNothing():
	""" we are really gonna do nothing here"""


for event in root.iter('Event_Birth'):
	event_id = first_last + "_" + strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + "_" + str(i)
	f.write("INSERT DATA { GRAPH <http://humanhistoryproject.ca/bakers> { <http://humanhistoryproject.ca/" + event_id + "> <http://humanhistoryproject.ca/hasSubject> <http://humanhistoryproject.ca/" + first_last + "> }}\n")
	try:
		birth = event.find('Birth').text
		if birth != None:	
			f.write('<http://humanhistoryproject.ca/' + event_id + '> <http://humanhistoryproject.ca/action> <http://humanhistoryproject.ca/birth> <http://humanhistoryproject.ca/Bakers> .\n')
	
	except AttributeError, TypeError:
		doNothing()
	
	try:
		death = event.find('Death').text
		if death != None:	
			f.write('<http://humanhistoryproject.ca/' + event_id + '> <http://humanhistoryproject.ca/action> <http://humanhistoryproject.ca/death> <http://humanhistoryproject.ca/Bakers> .\n')
	
	except AttributeError, TypeError:
		doNothing()


	try:
		Location = event.find('Location').text
		if Location != None:	
			f.write('<http://humanhistoryproject.ca/' + event_id + '> <http://humanhistoryproject.ca/hasLocation> <http://humanhistoryproject.ca/' + Location + '> <http://humanhistoryproject.ca/Bakers> .\n')
	
	except AttributeError, TypeError:
		doNothing()
	try:
		Date = event.find('Date').text
		if Date != None:		
			f.write('<http://humanhistoryproject.ca/' + event_id + '> <http://humanhistoryproject.ca/hasTime> <http://humanhistoryproject.ca/' + Date + '> <http://humanhistoryproject.ca/Bakers> .\n')
	
	except AttributeError, TypeError:
		doNothing()


	i += 1
