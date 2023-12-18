---
title: "Rapport Projet Web Sémantique"
author: "EL KATEB Sami, PAUL Thomas"
---

## Évolution de notre modélisation de rapports médicaux

Pour faire évoluer notre modélisation de rapports médicaux, nous avons commencé
par intégrer les retours reçus sur notre premier projet. 
Nous avons commencé par remplacer la propriété _gender_ par les classes Man et Woman. 
Puis nous avons ajouté les numéros de sécurité sociale des patients et les numéros
RPPS des médecins. 
Nous avons défini ces propriétés comme owl:InverseFunctionalProperty.
En effet, si deux entités ont la même valeur pour l'une de ces deux propriété, celles-ci sont identiques.
Pour la même raison, ce sont également les valeurs de owl:hasKey pour les patients et les médecins respectivement.

Puisque nous avions commencé à développer une ontologie OWL,
nous avons mis à jour la déclaration de notre ontologie en y ajoutant la référence à la version précédente.
Nous avons également corrigé nos erreurs précédentes où certaines propriétés définies comme ObjectProperty 
auraient dû être des DataProperty.

Nous avons ajouté à notre ontologie des liens de parenté tel que hasAncestor qui est une propriété asymétrique, irreflexive
et transitive et sa sous-propriété hasParent qui elle, n'est pas transitive. Nous avons également ajouté la 
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

Lors de la création de notre ontologie OWL nous avons définit les clés des patients comme étant 
leur numéro de sécurité sociale à l'aide de la propriété hasKey. Cette propriété exprime que 
deux instances ayant le même numéro de sécurité sociale sont la même instance. Nous pouvons vérifier 
l'effet de cette propriété en recherchant le poids du Patient7. En effet l'instance Patient7 ne
possède pas de propriété `weight`, cependant le Patient11 possédant le même numéro de
sécurité sociale possède cette propriété. Étant donné que les deux instances sont
considérées comme la même instance, nous pouvons récupérer le poids à partir du Patient7 (mcr_query_entailment 1). 
Le même effet est également atteint à en définissant la propriété ssn comme InverseFunctionalProperty.

Nous avons également définit les PersonWithGeneticDiabetesPredisposition comme étant
les personnes ayant un ancêtre atteint du diabète ou un sibling (frère/soeur) atteint du diabète.
Cependant les seules relations définies dans nos données sont les relations hasChild et hasBrother. 
La relation hasParent est inférée à partir de la relation hasChild dont elle est l'inverse. 
Celle-ci permet ensuite d'inférer la relation hasAncestor dont elle est la sous-classe.
La relation hasAncestor est transitive et s'applique donc sur plusieurs générations. Elle permet 
d'inférer des prédispositions génétiques à partir des diagnostiques effectués sur les grands-parents.
Ainsi en incluant uniquement les relations hasChild dans nos données,
le raisonneur OWL RL infère donc correctement que les patients 2, 8 et 9 qui ne sont pas diagnostiquée
diabétique ont une prédisposition génétique au diabète (mcr_query_entailment 2).

Enfin, nous retrouvons les maladies respiratoires que l'on peut mettre en evidence en
recherchant les différentes maladies respiratoires (mcr_query_entailment 3).
Celles-ci sont inférées comme étant l'union des maladies ayant
l'un des différents symptômes respiratoire. Et les équipes médicales qui sont
des équipes contenant au moins un médecin. Nous pouvons remarquer que les équipes
contenant des médecins sont inférées comme des équipes médicales alors que l'équipe 3
ne contenant aucun médecin n'est pas inférée.

## Contraintes SHACL 

Lors de notre projet initial, nous avions défini la classe "rapport de cas" 
(CaseReport) composée d'un médecin, un patient, un examen clinique et éventuellement une thérapie. 
Cette modélisation a évolué et ne contient plus de patient pour éviter la duplication
des données présentes dans l'examen clinique. 
Cette modélisation peut être affinée et contrainte à l'aide d'une contrainte SHACL. 
Nous avons donc définit `shapes:case_report` qui contraint les rapports
de cas à avoir au moins un Docteur et un examen clinique.
De même, nous avons définit les examens cliniques comme associés à un patient unique
et au minimum à un médecin dans la contrainte `shapes:clinical_examination`. 
Nous pouvons facilement vérifier que ces contraintes ont l'effet désiré en retirant le médecin de l'examen clinique
ou du rapport de cas ou en augmentant le nombre de patients.

L'une des évolutions de notre projet Web Sémantique a été l'ajout de 3 Thérausus. Pour 
standardiser les entités de ces thésaurus nous avons créé des contraintes SHACL pour les
médicaments, les signes et symptômes et les maladies. Ainsi, nous avons pus contraindre les instances
de ces classes à être incluses dans leur thésaurus respectif. De plus, nous avons
ajouté aux instances de la classe médicament d'avoir au moins une substance active une unité de médicament et une
forme galénique. De même, nous avons contraint les maladies à posséder au moins un signe clinique ou symptôme. Nous 
pouvons vérifier ces contraintes en retirant les propriétés requises ou en incluant des langues non supportées.

Finalement, nous avons définit des contraintes pour les médecins et les patients. Entre autres, les
instances de ces deux classes doivent être identifiée respectivement par un numéro RPPS et un numéro de sécurité de sécurité sociale.
Le format de ces numéros est contrôlé à l'aide d'expressions régulières. Nous pouvons utiliser des numéros invalide pour 
contrôler le bon fonctionnement de ces contraintes.
