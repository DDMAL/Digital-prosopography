Digital-prosopography
=====================

Prosopography project using Gate and RDF

This project aims for extracting entities using Gate and querying database using RDF.

### Gate

Contains all gate programming files, namely .jape .java .python files

### Gate_Extracted

Contains all Extracted files with name entities. Namely .xml files

It has two sub directories-- raw_xml and preserving. 

raw_xml contains all xml files with specification of every single nodes and features. 
It is the xml file rdf is gonna deal with in the end.

preserving contains all xml files with no specification but only the annotation being used. 
It does not contain any feature which makes them sort of useless to look at. But they are a lot cleaner and relatively small,
so github can display them (raw_xml files are normally too big to display)
    

### rdf

Contains all rdf description files
