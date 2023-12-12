# Owl list of propert

To do :
- Transform gender into male or female (owl:disjointWith)

## List of properties
- owl:ObjectProperty
- owl:DatatypeProperty
- owl:AnnotationProperty (not important)

- owl:SymmetricProperty
- owl:TransitiveProperty
- owl:propertyDisjointWith

- owl:ReflexiveProperty

- owl:propertyDisjointWith

- owl:propertyChainAxiom
- owl:FunctionalProperty
- owl:InverseFunctionalProperty

## Class relationships
- enumerated classes : owl:oneOf
- class union : owl:unionOf
- class intersection : owl:intersectionOf
- class negation : owl:complementOf
- disjonction between two classes : owl:disjointWith
- disjonction between several classes owl:AllDisjointClasses and owl:members
- disjoint union : owl:disjointUnionOf

## Equivalences and alignements
- owl:sameAs
- owl:differentFrom
- owl:hasKey

## Property restrictions
- restriction of property values
- restriction of some property values
- restriction to a single property value
- restriction of a property value to its subject
- cardinality restriction

Done :
- owl:equivalentClass (done during previous project)
- owl:equivalentProperty (done during previous project)
- owl:AsymmetricProperty (:hasDoctor and :hasPatient)
- owl:inverseOf (:hasDoctor and :hasPatient)
- owl:IrreflexiveProperty (:hasPatient a patient cannot be the patient of itself but a Doctor technically can diagnose itself)
