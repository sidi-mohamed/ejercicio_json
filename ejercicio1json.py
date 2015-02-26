import json
fich=open('asociaciones.json')
doc= json.load(fich)

#1. programa que lista todos los nombres de las asociaciones

for x in doc["asociacions"]["asociacion"]:
	print x["nombre"]

#2. programa que muestre el total de de asociaciones 

for x in doc["asociacions"]["asociacion"]:
	print len(x["nombre"])


#programa que le indiques el barrio y te imprima las asociaciones que hay en el 





# programa que me imprima todos los correos de las asociaciones
for x in doc["asociacions"]["asociacion"]:
	print (x["nombre"])
	print (x["correo-electronico"])