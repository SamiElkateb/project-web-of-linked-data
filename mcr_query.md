1. Quelles sont les maladies pouvant avoir comme signe clinique la fièvre ?
```sparql
prefix : <http://project-wold.fr/schema#>
prefix symptoms: <http://project-wold.fr/symptoms/data#>

SELECT ?disease
WHERE {
    ?disease :signOrSymptom symptoms:Fever
}
```

2. Quel sont les 3 signes ou symptômes les plus présents ?
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

3. Quelles sont les maladies ayant pour symptôme la fatigue mais n'étant pas traités par l'Amoxicilline ?
```sparql
prefix : <http://project-wold.fr/schema#>
prefix symptoms: <http://project-wold.fr/symptoms/data#>
prefix treatments: <http://project-wold.fr/treatments/data#>

SELECT ?disease
WHERE {
    ?disease :signOrSymptom symptoms:Fatigue .
    MINUS { 
        ?disease :possibleTreatment treatments:AmoxicillinPrescription .
    }
}
```


4. Quel est le nom de famille du médecin effectuant le plus de prescription de paracétamol ?
```sparql
prefix : <http://project-wold.fr/schema#>
prefix treatments: <http://project-wold.fr/treatments/data#> 

SELECT ?doctorName (COUNT(?doctor) AS ?numberParacetamolPrescription)
WHERE {
    ?case_report a :CaseReport ;
            :hasDoctor ?doctor ;
            :hasMedicalTherapy treatments:ParacetamolPrescription .
    ?doctor :familyName ?doctorName .
}
GROUP BY ?doctorName
ORDER BY DESC(?numberParacetamolPrescription)
LIMIT 1
```

5. Quels sont les patients dont l'examen clinique a été réalisé par un praticien autre que celui du rapport de cas ?
```sparql
prefix : <http://project-wold.fr/schema#>
prefix reports: <http://project-wold.fr/case_reports/data#>

SELECT ?patient ?doctor1 ?doctor2
WHERE {

    ?examination a :ClinicalExamination ;
            :hasPatient ?patient ;
            :hasDoctor ?doctor1 .

    ?case a :CaseReport ;
            :hasClinicalExamination ?examination ;
            :hasPatient ?patient ;
            :hasDoctor ?doctor2 .

    FILTER (?doctor1 != ?doctor2)
}
```

6. Quels sont les patients ayant plus de 60 ans ?
référence: https://stackoverflow.com/questions/74532061/how-to-get-todays-date-in-sparql
```sparql
prefix : <http://project-wold.fr/schema#>
SELECT ?patient ?birthDate
WHERE {
    ?patient a :Patient ;
             :birthDate ?birthDate .

    BIND(now() AS ?currentDateTime) .
    BIND(year(?currentDateTime) - 60 AS ?sixtyYearsAgo) .
    BIND(CONCAT(STR(?sixtyYearsAgo), "-",
                STR(month(?currentDateTime)), "-",
                STR(day(?currentDateTime))) AS ?limitDate) .
    FILTER (?birthDate < ?limitDate)
}
```

7. Quels sont les rapports de cas ayant eu besoin d'examens complémentaire (Medical Test) ?
```sparql
prefix : <http://project-wold.fr/schema#>
prefix reports: <http://project-wold.fr/case_reports/data#>

SELECT ?examination ?test
WHERE {

    ?examination a :ClinicalExamination ;
            :hasMedicalTest ?test .
}
```

8. Quels ont été les examens cliniques ayant les mêmes symptômes mais des maladies différentes?


9. Générer une relation hasDoctor entre les patients et les docteurs assignés à leur case report

10. 
