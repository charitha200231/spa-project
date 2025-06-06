import csv
import json
import dicttoxml

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

with open('output.json', 'w') as jf:
    json.dump(data, jf, indent=2)

xml_data = dicttoxml.dicttoxml(data)
with open('output.xml', 'wb') as xf:
    xf.write(xml_data)
