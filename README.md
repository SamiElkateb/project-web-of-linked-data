# Projet
https://lov.okfn.org/dataset/lov/  
https://lov.linkeddata.es/dataset/lov/vocabs/medred  
https://lov.linkeddata.es/dataset/lov/vocabs/obo  

##  Section 1
Propose an RDFS model for describing medical case reports.   
You may reuse existing ontologies and complement them with your own schema (mcr_schema.ttl).
- https://en.wikipedia.org/wiki/Case_report
- https://fr.wikipedia.org/wiki/Observation_m%C3%A9dicale
- https://fr.wikipedia.org/wiki/Examen_clinique
- https://fr.wikipedia.org/wiki/Examen_compl%C3%A9mentaire

##  Section 2
Write a short report (mcr_report.pdf) presenting in natural language your modeling choices.

##  Section 3
Write an RDF graph (mcr_data_.ttl) describing medical case reports of a few people.  
- Describe the data in one or several RDF graphs, stored in a file mcr_data.ttl or files mcr_data_xxx.ttl. 
  Possibly link your data to RDF graphs from the Linked Open Data (e.g. DBpedia).
- Describe your model in one or several RDFS vocabulary(ies), stored in file(s) mcr_schema.ttl or mcr_schema_xxx.ttl. 
  Possibly reuse exististing vocabularies from the Web of Linked Data (e.g. FOAF, SOSA) and complete it with your own vocabulary.
- Provide a version of your RDF graph in JSON (data.json)
- Write an HTML page (data_presentation.html) presenting (part of) your data to human users 
  (if you are not fluent with HTML do not spend too much time writing a complicated stylesheet) and containing (part of) your RDF graph in RDFa.

##  Section 4
Write 10 interesting SPARQL queries implementing competency questions dealing with case report. 
Store all of them in a single file mcr_query.txt where, for each one, 
indicate in natural language the competency question it implements.


Upload a single zip file containing your entire work.



## SKOS?
https://www.w3.org/2001/sw/wiki/SKOS/Datasets#Drug_Administration_Forms  
Drug Administration Forms  
Clinical drug administration forms mapped to SNOMED CT and FDA codes: http://www.agfa.com/w3c/2009/drugAdministrationForms#  
