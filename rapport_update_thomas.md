Nous avons pu définir ces propriétés en tant que owl:InverseFunctionalProperty 
car deux entités ayant la même valeur pour l'une de ces deux propriété implique que les entités sont 
identique. 
---> (proposition peut etre trop simpliciste mais j'avais du mal a comprendre ta version même en relisant plusieurs fois)
Nous avons pu définir ces propriétés en tant que owl:InverseFunctionalProperty car deux entités qui ont la 
même valeur, implique que le sujet est le même.


Nous avons également corrigé les erreurs que nous avions faites concernant les propriétés 
que nous avions définies comme ObjectProperty alors que celles-ci étaient des DataProperty.
--->
Nous avons également corrigé les erreurs que nous avions faites concernant les propriétés 
définies comme ObjectProperty alors que celles-ci étaient des DataProperty.


Nous avons ajouté à notre ontologie des liens de parenté tel que hasAncestor qui est une propriété asymétrique, irreflexive
et transitive et sa sous-propriété hasParent qui n'est elle pas transitive.
--->
Nous avons ajouté à notre ontologie des liens de parenté tels que hasAncestor qui est une propriété asymétrique, irreflexive
et transitive et sa sous-propriété hasParent qui elle, n'est pas transitive.


En effet l'instance Patient7 ne possède pas de propriété `weight`, cependant le Patient11 possédant le même numéro de
sécurité sociale possède cette propriété
--->
pas compris, y'a trop de possède^^


Et les équipes médicales qui sont des équipes contenant au moins un médecin. Nous pouvons remarquer que les équipes
contenant des médecins sont inférées comme des équipes médicales alors que l'équipe 3
ne contenant pas de médecin ne l'est pas.
--->
Les équipes médicales sont des équipes qui contiennent au moins un médecin. 
Nous pouvons remarquer que les équipes contenant des médecins sont inférées 
comme des équipes médicales alors que l'équipe 3 ne contenant aucun médecin 
n'est pas inférée.