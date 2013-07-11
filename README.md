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





package sheffield.examples;
import gate.Document;
import gate.Corpus;
import gate.CorpusController;
import gate.AnnotationSet;
import gate.Gate;
import gate.Factory;
import gate.util.persistence.PersistenceManager;

import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;
import java.util.Iterator;

import java.io.File;
import java.io.FileOutputStream;
import java.io.BufferedOutputStream;
import java.io.OutputStreamWriter;

public class BatchProcessApp {
	
	public static void main(String[] args) throws Exception {
 
	    parseCommandLine(args);

	    // initialize GATE - this must be done before calling any GATE APIs
	    Gate.init();

	    // load the saved application
	    CorpusController application =
	      (CorpusController)PersistenceManager.loadObjectFromFile(gappFile);

	    // Create a Corpus to use.  We recycle the same Corpus object for each
	    // iteration.  The string parameter to newCorpus() is simply the
	    // GATE-internal name to use for the corpus.  It has no particular
	    // significance.
	    Corpus corpus = Factory.newCorpus("BatchProcessApp Corpus");
	    application.setCorpus(corpus);

	    // process the files one by one
	    for(int i = firstFile; i < args.length; i++) {
	      // load the document (using the specified encoding if one was given)
	    	System.out.println(args[i]);
	      File docFile = new File("/Users/lhua/Documents/Digital-prosopography/Gate_Extracted/bakers/" + args[i]);
	      System.out.print("Processing document " + docFile + "...");
	     Document doc = Factory.newDocument(docFile.toURL(), encoding);

	      // put the document in the corpus
	      corpus.add(doc);
	      
	      // run the application
	      application.execute();

	      // remove the document from the corpus again
	      corpus.clear();

	      String docXMLString = null;
	      // if we want to just write out specific annotation types, we must
	      // extract the annotations into a Set
	      if(annotTypesToWrite != null) {
	        // Create a temporary Set to hold the annotations we wish to write out
	        Set annotationsToWrite = new HashSet();
	        
	        // we only extract annotations from the default (unnamed) AnnotationSet
	        // in this example
	        AnnotationSet defaultAnnots = doc.getAnnotations();
	        Iterator annotTypesIt = annotTypesToWrite.iterator();
	        while(annotTypesIt.hasNext()) {
	          // extract all the annotations of each requested type and add them to
	          // the temporary set
	          AnnotationSet annotsOfThisType =
	              defaultAnnots.get((String)annotTypesIt.next());
	          if(annotsOfThisType != null) {
	            annotationsToWrite.addAll(annotsOfThisType);
	          }
	        }

	        // create the XML string using these annotations
	        docXMLString = doc.toXml(annotationsToWrite);
	      }
	      // otherwise, just write out the whole document as GateXML
	      else {
	        docXMLString = doc.toXml();
	      }

	      // Release the document, as it is no longer needed
	      Factory.deleteResource(doc);

	      // output the XML to <inputFile>.out.xml
	      String outputFileName = docFile.getName() + ".xml";
	      File outputFile = new File(docFile.getParentFile(), outputFileName);

	      // Write output files using the same encoding as the original
	      FileOutputStream fos = new FileOutputStream(outputFile);
	      BufferedOutputStream bos = new BufferedOutputStream(fos);
	      OutputStreamWriter out;
	      if(encoding == null) {
	        out = new OutputStreamWriter(bos);
	      }
	      else {
	        out = new OutputStreamWriter(bos, encoding);
	      }

	      out.write(docXMLString);
	      
	      out.close();
	      System.out.println("done");
	    } // for each file

	    System.out.println("All done");
	  } // void main(String[] args)


	  /**
	   * Parse command line options.
	   */
	  private static void parseCommandLine(String[] args) throws Exception {
	    int i;
	    // iterate over all options (arguments starting with '-')
	    for(i = 0; i < args.length && args[i].charAt(0) == '-'; i++) {
	      switch(args[i].charAt(1)) {
	        // -a type = write out annotations of type a.
	        case 'a':
	          if(annotTypesToWrite == null) annotTypesToWrite = new ArrayList();
	          annotTypesToWrite.add(args[++i]);
	          break;

	        // -g gappFile = path to the saved application
	        case 'g':
	          gappFile = new File(args[++i]);
	          break;

	        // -e encoding = character encoding for documents
	        case 'e':
	          encoding = args[++i];
	          break;

	        default:
	          System.err.println("Unrecognised option " + args[i]);
	          usage();
	      }
	    }

	    // set index of the first non-option argument, which we take as the first
	    // file to process
	    firstFile = i;

	    // sanity check other arguments
	    if(gappFile == null) {
	      System.err.println("No .gapp file specified");
	      usage();
	    }
	  }

	  /**
	   * Print a usage message and exit.
	   */
	  private static final void usage() {
	    System.err.println(
	   "Usage:\n" +
	   "   java sheffield.examples.BatchProcessApp -g <gappFile> [-e encoding]\n" +
	   "            [-a annotType] [-a annotType] file1 file2 ... fileN\n" +
	   "\n" +
	   "-g gappFile : (required) the path to the saved application state we are\n" +
	   "              to run over the given documents.  This application must be\n" +
	   "              a \"corpus pipeline\" or a \"conditional corpus pipeline\".\n" +
	   "\n" + 
	   "-e encoding : (optional) the character encoding of the source documents.\n" +
	   "              If not specified, the platform default encoding (currently\n" +
	   "              \"" + System.getProperty("file.encoding") + "\") is assumed.\n" +
	   "\n" + 
	   "-a type     : (optional) write out just the annotations of this type as\n" +
	   "              inline XML tags.  Multiple -a options are allowed, and\n" +
	   "              annotations of all the specified types will be output.\n" +
	   "              This is the equivalent of \"save preserving format\" in the\n" +
	   "              GATE GUI.  If no -a option is given the whole of each\n" +
	   "              processed document will be output as GateXML (the equivalent\n" +
	   "              of \"save as XML\")."
	   );

	    System.exit(1);
	  }

	  /** Index of the first non-option argument on the command line. */
	  private static int firstFile = 0;

	  /** Path to the saved application file. */
	  private static File gappFile = null;

	  /** 
	   * List of annotation types to write out.  If null, write everything as
	   * GateXML.
	   */
	  private static List annotTypesToWrite = null;

	  /**
	   * The character encoding to use when loading the docments.  If null, the
	   * platform default encoding is used.
	   */
	  private static String encoding = null;

}







-g ichwithperson.gapp -a Date -a Location -a Birth -a Death -a JobTitle -a Object -a Verb -a event
Aaron_Pietro.txt
Adams_Thomas.txt
Aaron_abbot_of_the_monasteries_of_St..txt 
Adaskin_Harry.txt
Aavik_Juhan.txt                                 Addinsell_Richard.txt
Abaco_Evaristo_Felice_dalT.txt                  Adelburg_August_Ritter_von.txt
Abaco_Joseph_Marie_Clement.txt                  Adgate_Andrew.txt
Abbado_Marcello.txt                             Adler_Clarence.txt
Abbatini_Antonio_Maria.txt                      Adler_F._Charles.txt
Abbey_John.txt                                  Adler_Guido.txt
Abbott_Emma.txt                                 Adler_Kurt.txt
Abe_Komei.txt                                   Adler_Kurt_Herbert.txt
Abeille_Johann_Christian_Ludwig.txt             Adler_Larry_(Lawrence).txt
Abel_Karl_Friedrich.txt                         Adler_Peter_Herman.txt
Abel_Ludwig.txt                                 Adler_Samuel.txt
Abell_Arthur_M..txt                             Adlgasser_Anton_Cajetan.txt
Abell_John.txt                                  Adlung_Jakob.txt
Abendroth_Hermann.txt                           Adorno_Theodor_(real_name_Wiesen-.txt
Aber_Adolf.txt                                  Adriaensen_Emanuel_(called_Hadrianus).txt
Abert_Anna_Amalie.txt                           Adrio_Adam.txt
Abert_Hermann.txt                               Aerts_(ahrts)_Egide.txt
Abert_Johann_Joseph.txt                         Aeschbacher_Adrian.txt
Abos_Girolamo_(baptismal_name_Geroni-.txt       Aeschbacher_Niklaus.txt
Abraham_Gerald.txt                              Aeschbacher_Walther.txt
Abraham_Max.txt                                 Afanassiev_(ah-fah-nah'-syev)_Nikolay_Ya-.txt
Abraham_Otto.txt                                Afranio_de_Pavia_(family_name_Albonese)_.txt
Abranyi_Cornelius.txt                           Agazzari_(ah-gaht-sah'-re)_Agostino.txt
Abranyi_Emil.txt                                Agnew_Roy.txt
Abravanel_Maurice.txt                           Agostini_Lodovico.txt
Absil_Jean.txt                                  Agostini_Mezio.txt
Abt_Franz.txt                                   Agostini_Paolo.txt
Achron_Isidor.txt                               Agostini_Pietro_Simone.txt
Achron_Joseph.txt                               Agrell_Johan_Joachim.txt
Ackte_(real_name_Achte).txt                     Agricola_Alexander.txt
Adam_(ah-dahn)_Adolphe-Charles.txt              Agricola_Johann_Friedrich.txt
Adam_de_la_Hale_(or_Halle)_called.txt           Agricola_Martin.txt
Adam_von_Fulda_German_theorist_and.txt          Aguado_Dionisio.txt
Adam_Claus.txt                                  Aguilar_(ah-ghe-lahr')_Emanuel_Abra-.txt
Adam_Jeno.txt                                   Aguilera_de_Heredia_Sebastian.txt
Adam_Louis;_Alsatian_pianist.txt                Aguirre_(ah-ger'-re)_Julian.txt
Adamowski_(ah-dah-mov'-ske)_Joseph.txt          Agujari_(ah-goo-yah'-re)_Lucrezia.txt
Adamowski_Timothee.txt                          Ahle_Johann_Georg.txt
Adams_Charles.txt                               Aragon_c._1565;_d._in_Saragossa_after_1620..txt
Adams_Suzanne.txt