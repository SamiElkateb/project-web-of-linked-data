---
title: "Rapport Projet Web Sémantique"
author: "EL KATEB Sami, PAUL Thomas"
---

[ ] La patient est lié inutilement à casereport et examination qui sont déjà liées
[ ] Il faudrait avoir au moins un patient qui a plusieurs consultations et examens


## Évolution de notre modélisation de rapports médicaux

Pour faire évoluer notre modélisation de rapports médicaux, nous avons commencé
par intégrer les retours reçus sur notre premier projet. 
Nous avons donc remplacé la propriété gender par les classes Man et Woman. Puis
nous avons ajouté les numéros de sécurité sociale des patient et les numéros
RPPS des médecins.

De plus, comme nous avions débuté une ontology owl, nous avons avons mis à jour la déclaration
de notre ontology en ajoutant la référence à la version précédente.
Nous avons également corrigé les erreurs que nous avions faites concernant les propriétés 
que nous avions définies comme ObjectProperty alors que celles-ci étaient des DataProperty.

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
