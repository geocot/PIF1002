#Démonstration pour le cours PIF1002 UQTR
#Martin Couture
#Mars 2024
#Besoin de l'objet Meteo disponible ici: https://github.com/geocot/Scripts_Cours_Introduction_Python/blob/master/meteoPython/objMeteo.py

import arcpy, objMeteo, os
arcpy.env.overwriteOutput = True
fichierSHP = "stationsQC.shp"
def lectureMeteo(url):
    meteo = objMeteo.Meteo(url)
    meteo.lireMeteo()
    return [(meteo.temperature).replace("°C", ""), meteo.condition]

cursor = arcpy.UpdateCursor(os.getcwd() + "\\" + fichierSHP)
for row in cursor:
    print(row.Nom)
    lecture = lectureMeteo(row.xml)
    print("Temp: {} Cond: {}".format( lecture[0], lecture[1]))
    row.setValue("Temp", lecture[0])
    row.setValue("Cond", lecture[1])
    cursor.updateRow(row) #Mise à jour de la ligne
