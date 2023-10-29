1. Quel sont les 3 signes ou symptômes les plus présents ?
```sparql
prefix : <http://project-wold.fr/schema#>

SELECT ?symptom (COUNT(?symptom) AS ?count)
WHERE {
    ?exam a :ClinicalExamination ;
            :hasSignOrSymptom ?symptom .
}
GROUP BY ?symptom
ORDER BY DESC(?count)
LIMIT 3
```

2. Quelles sont les maladies pouvant avoir comme signe clinique la fièvre ?
```sparql
prefix : <http://project-wold.fr/schema#>
prefix symptoms: <http://project-wold.fr/symptoms/data#>

SELECT ?disease
WHERE {
    ?disease :signOrSymptom symptoms:Fever
}
```

3. Quelles sont les maladies ayant pour symptôme la fatigue mais n'étant pas traités par l'Amoxicilline ?

4. Quel est le médecin effectuant le plus de prescription de paracétamol ?

5. Quels sont les patients dont l'examen clinique a été réalisé par un praticien autre que celui du rapport de cas ?

6. Quels sont les patients ayant plus de 60 ans ?

7. Quels sont les rapports de cas ayant eu besoin d'examens complémentaire ?

8. Quels ont été les examens cliniques ayant les mêmes symptômes mais des maladies différentes?

9. Générer une relation hasDoctor entre les patients et les docteurs assignés à leur case report

10. 
