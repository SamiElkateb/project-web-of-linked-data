---
title: "Rapport Projet Web Sémantique"
author: "EL KATEB Sami, PAUL Thomas"
---

[ ] La patient est lié inutilement à casereport et examination qui sont déjà liées
[ ] Il faudrait avoir au moins un patient qui a plusieurs consultations et examens


## Évolution de notre modélisation de rapports médicaux

Pour faire évoluer notre modélisation de rapports médicaux, nous avons commencé
par intégrer les retours reçus sur notre premier projet. 
Nous avons donc remplacé la propriété _gender_ par les classes Man et Woman. 

Puis nous avons ajouté les numéros de sécurité sociale des patients et les numéros
RPPS des médecins. 
Nous avons pu définir ces propriétés en tant que owl:InverseFunctionalProperty 
car deux entités ayant la même valeur pour l'une de ces deux propriété implique que les entités sont 
identique. 
Par conséquent, nous avons également pu les définir comme valeur de owl:hasKey
pour les patients et les médecins respectivement.

Étant donné que nous avions débuté une ontology owl, nous avons avons mis à jour la déclaration
de notre ontology en ajoutant la référence à la version précédente.
Nous avons également corrigé les erreurs que nous avions faites concernant les propriétés 
que nous avions définies comme ObjectProperty alors que celles-ci étaient des DataProperty.

Nous avons ajouté à notre ontologie des liens de parenté tel que hasAncestor qui est une propriété asymétrique, irreflexive
et transitive et sa sous-propriété hasParent qui n'est elle pas transitive. Nous avons également ajouté la 
propriété hasChild qui est l'inverse de hasParent et possède les mêmes types que celle-ci. De plus, nous
avons ajouté la propriété hasBrother et hasSister toutes deux disjointes et irréflexives, sous-propriété de hasSibling.

Ces liens de parenté nous permettent de mettre en évidence les prédispositions génétiques. Nous 
avons ainsi pu créer la classe PersonWithGeneticDiabetesPredisposition qui inclus les personnes ayant un ancêtre
diabétique ou un frère/soeur diabétique. Nous avons choisit de ne pas exclure les personnes diagnostiquées diabétique 
de cet ensemble car nous considérons que celles-ci sont toujours des personnes prédisposées génétiquement au diabète.

Par la suite nous avons définit l'ensemble des maladies respiratoires (RespiratoryCondition) comme l'union des maladies ayant pour symptôme la toux,
l'essoufflement ou le mal de gorge. Nous avons également définit l'ensemble des maladies infectieuse et son complément, l'ensemble des maladies non
infectieuses.

Finalement, nous avons définit une équipe (Team) puis une équipe médicale (MedicalTeam) comme étant une équipe composée
d'au moins un médecin.

Nous avons également introduit 3 thésaurus SKOS dans nos données: un thésaurus de médicament, un thésaurus de symptômes et un
thésaurus des maladies.
Ceux-ci se prêtent bien à être organisés dans un thésaurus car ils peuvent facilement être classés de manières
hiérarchiques (différentes familles de médicaments, différents types de symptômes et de maladies). De plus les thésaurus permettent
d'établir des relations entre les différents termes. Enfin la création de thésaurus permet de normaliser la terminologie.
Nous avons également créé une collection de maladies contagieuses qui permet de regrouper les maladies
à travers leur contagiosité alors que le thesaurus est lui organisé par organe atteint. 

## OWL Entailment

Ainsi en incluant uniquement les relations hasChild dans nos données,
le raisonneur OWL RL infère que la propriété inverse de hasChild est hasParent qui est elle même 
une sous-propriété de hasAncestor et infère donc correctement que Patient9 qui n'est pas diagnostiquée
diabètique a une prédisposition génétique au diabète.


Nous retrouvons dans les maladies respiratoire ...

## 
