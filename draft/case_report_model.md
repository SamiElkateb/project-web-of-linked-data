Global:
- type: 
    - An unexpected association between diseases or symptoms.
    - An unexpected event in the course of observing or treating a patient.
    - Findings that shed new light on the possible pathogenesis of a disease or an adverse effect.
    - Unique or rare features of a disease.
    - Unique therapeutic approaches.
    - A positional or quantitative variation of the anatomical structures.

Usually:
For an individual patient -> https://schema.org/Patient
detailed report of the 
Examen clinique: 
- symptoms, 
- signs, -> https://schema.org/MedicalSign
- diagnosis, 
+ Examens complémentaires -> https://schema.org/MedicalTest -> https://schema.org/ImagingTest

https://schema.org/MedicalTherapy
    - treatment,  
    - follow-up
    - adverse events -> https://schema.org/adverseOutcome
- effectiveness
// cost

Optional:
- demographic profile of the patient https://schema.org/Patient
- literature review of other reported cases

Case report and review of the literature:
- extensive review of the relevant literature on the topic at-hand
- a systematic review of available evidence -> https://schema.org/MedicalStudy


status: published or not

CARE (i.e. CAse REport) guidelines include a reporting checklist that is listed on the:
introduction, patient information, clinical findings, timeline, diagnostic assessment, therapeutic interventions, follow-up and outcomes, discussion, patient perspective, and informed consent.

+ Medecin



- medical device: https://schema.org/MedicalDevice
