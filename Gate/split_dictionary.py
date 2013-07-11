import os
import re

f=open('bakers.txt', 'r')
flag = 1
p = re.compile(r'\s+')

for line in f:
	if flag == 1:
		if line != "\n":
			arr = line.split(",")
			f_name = arr[0].strip() + "_" + arr[1].strip().replace(" ", "_") + ".txt"
			sec_f = open("../Gate_Extracted/bakers/" + f_name, 'w+')
			
			line = line.rstrip()
			l = line.split("-")
			if len(l)>1:
				print l
				line = l[0]
			else:
				line += " "

			#print repr(line)
			sec_f.write(line)
			flag = 0;
	else:
		if line == "\n":
			flag = 1
			sec_f.close()
			print "file " + f_name + " written"
		else:
			line = line.rstrip()
			l = line.split("-")
			print l
			if len(l)>1:
				line = l[0]
			else:
				line += " "
			#print repr(line)
			sec_f.write(line)







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
"""


