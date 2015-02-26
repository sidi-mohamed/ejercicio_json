import json
fich=open('asociaciones.json')
doc= json.load(fich)

#1. programa que lista todos los nombres de las asociaciones

for x in doc["asociacions"]["asociacion"]:
	print x["nombre"]






