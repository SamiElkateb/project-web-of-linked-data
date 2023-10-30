# Rapport sur les choix de modélisation
Lors de l'élaboration de notre modèle RDFS destiné à décrire les rapports de cas médicaux,
nous avons consulté diverses sources, notamment les pages Wikipedia relatives à l'observation médicale, 
l'examen clinique et l'examen complémentaire. 
Nous avons également choisit de nous appuyer au maximum sur des ontologies existantes, en les étendant lorsque nécessaire.

Ainsi, nous avons défini une classe intitulée "rapport de cas" (CaseReport) qui nous permet de typer nos ressources. Nous lui associons un patient, 
un médecin, un examen clinique et une thérapie.
Pour ce faire, nous avons introduit les propriétés hasClinicalExamination (a un examen clinique), 
hasDoctor, hasPatient et hasMedicalTherapy (a un traitement médical). 
Nous avons choisi de spécifier uniquement la range de ces propriétés, car elles peuvent s'appliquer à de nombreux domaines. 
Par exemple, nous pouvons lier un patient à un examen clinique dont il est le sujet ou à un médecin qui le prend en charge.

Dans notre modèle, nous avons intégré les classes "patient" et "traitement médical" (Medical Therapy) de l'ontologie de schema.org.
Toutefois, nous avons créé une classe spécifique pour l'examen clinique.
Pour le médecin, nous avons créé une classe distincte que nous avons étendu de la classe Person de schema.org.

Un examen clinique a pour objectif d'identifier des signes et symptômes cliniques afin de poser un diagnostic. 
Par conséquent, nous avons ajouté à notre ontologie les propriétés hasSignOrSymptom, hasMedicalTest (a un examen complémentaire) et hasDiagnosis. 
La propriété hasSignOrSymptom sert à relier notre examen clinique aux signes et symptômes de l'ontologie.
La propriété hasMedicalTest peut le relier à des examens complémentaires, tandis que la propriété hasDiagnosis permet de lui associer une pathologie (diseases).
De plus, nous associons un examen clinique à un médecin et à un patient à l'aide des propriété hasPatient et hasDoctor. 
Toutes ces classes excepté la classe Doctor proviennent de l'ontologie schema.org.

