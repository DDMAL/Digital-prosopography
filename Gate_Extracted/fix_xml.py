import os
import sys
import re
import xml.etree.ElementTree as ET


def doNothing():
	"""yeah we are doing nothing here"""

def findElement(tag, f):
	try:
		string = event.find(tag).text
		if string != None:
			f.write('<'+tag+'>' + string + '</'+tag+'>')
	
	except AttributeError, TypeError:
		doNothing()

fileIn = "bakers_extracted/" + sys.argv[1]
fileout = "bakers_fixed/" + sys.argv[1]

f = open(fileout, "w+")
tree = ET.parse(fileIn)
root = tree.getroot()

for event in root.iter('event'):
	objectflag=0
	verbflag=0
	f.write('<event>')
	
	for obj in event.findall('Object'):
		try:
			Object = obj.text
			try:
				subloc = obj.find('Location').text
				if subloc != None:
					if Object != None:
						f.write('<Location>' + Object + subloc + '</Location>')
						objectflag = 1
					else:
						f.write('<Location>' + subloc + '</Location>')
			except AttributeError, TypeError:
				doNothing()
			try:
				subjob = obj.find('JobTitle').text
				if subjob != None:
					f.write('<Verb>JobTitle</Verb>') 
					verbflag = 1
					if Object != None:
						f.write('<JobTitle>' + Object + subjob + '</JobTitle>')
						objectflag = 1
					else:
						f.write('<JobTitle>' + subjob + '</JobTitle>')
			except AttributeError, TypeError:
				doNothing()
			if Object != None and objectflag == 0:
				f.write('<Object>' + Object + '</Object>')

		except AttributeError, TypeError:
			doNothing()
	
	try:
		Location = event.find('Location').text
		Object = event.find('Location').find('Object').text
		if Location != None:
			if Object != None:
				f.write('<Location>' + Object + '</Location>')
			else:
				f.write('<Location>' + Location + '</Location>')
	
	except AttributeError, TypeError:
		doNothing()

	try:
		JobTitle = event.find('JobTitle').text
		Object = event.find('JobTitle').find('Object').text
		if JobTitle != None:
			if Object != None:
				f.write('<JobTitle>' + Object + '</JobTitle>')
			else:
				f.write('<JobTitle>' + JobTitle + '</JobTitle>')
	except AttributeError, TypeError:
		doNothing()

	try:
		if event.find('Birth').text != None:
			f.write('<Verb>be born</Verb>')
	
	except AttributeError, TypeError:
		doNothing()

	try:
		if event.find('Death').text != None:
			f.write('<Verb>died</Verb>')
	
	except AttributeError, TypeError:
		doNothing()

	findElement('Date', f)
	if verbflag==0:
		findElement('Verb', f)


	f.write('</event>')

f.close()
