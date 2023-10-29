import requests
import json

filenames = [
    "draft/case_reports.ttl",
    "draft/diseases.ttl",
    "draft/doctors.ttl",
    "draft/drugs.ttl",
    "draft/medical_tests.ttl",
    "draft/patients.ttl",
    "draft/signsOrSymptoms.ttl",
    "draft/treatments.ttl",
]
with open("full_data.ttl", "w") as outfile:
    for index, fname in enumerate(filenames):
        with open(fname) as infile:
            for line in infile:
                if index > 0 and line.startswith("@prefix"):
                    continue
                outfile.write(line)


url = "https://www.easyrdf.org/converter"
file_data = ""
with open("full_data.ttl", "r") as file:
    file_data = file.read()

data_payload = {
    "data": file_data,
    "uri": "http://njh.me/",
    "in": "turtle",
    "out": "jsonld",
    "raw": "1",
}

response = requests.post(url, data=data_payload)

parsed_json = response.json()

with open('data.json', 'w') as outfile:
    json.dump(parsed_json, outfile, indent=4)
