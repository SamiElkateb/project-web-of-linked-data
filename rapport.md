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
avons ajouté la propriété hasBrother et 

Ces liens de parenté nous permettre de mettre en évidence les prédispositions génétiques. Nous 
avons ainsi pu créer la classe PersonWithGeneticDiabetesPredisposition qui inclus les personnes ayant un ancêtre
diabétique ou un frère/soeur diabétique. 



-- draft
parler de:

- on a définit rpps et ssn comme InverseFunctionalProperty
- on a utilisé ssn et rpps en haskey ainsi deux personnes ayant le même ssn sont la même personne et de même pour le rpps et les médecin.

- on a définit une equipe puis une équipe médicale comme étant une équipe composée uniquement de médecins
- on a définit InfectiousDisease et son complémentaire NonInfectiousDisease

on a ajouter des liens de parenté entre les patients:

ces liens de parentés nous permettent de mettre en évidence des potentielles prédisposition génétiques.
Ainsi nous avons définit une personne prédisposée à avoir le diabète comme l'union des personnes ayant un ancestre diabétique 
et celui des frères/soeurs ayant le diabète (siblings)


Nous avons définit les maladies respiratoires comme l'union des maladies ayant pour symptome la toux, l'essoufflement ou
le mal de gorge.

skos: 
parler de:

- on a créé 2 thésaurus: un thésaurus de médicament et un thésaurus de symptomes.
ceux-ci se prettent bien à être organisés dans un thésaurus car ils peuvent facilement être classés de manières
hiérarchiques (différentes familles de médicaments, différents types de symptômes). De plus les thésaurus permettent
d'établir des relations entre les différents termes. Enfin la création de thésaurus permet de normaliser la terminologie.
Nous avons ainsi
- on a créé une collection de maladies

## OWL Entailment

## 
