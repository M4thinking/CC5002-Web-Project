# -*- coding: utf-8 -*-
import cgi
import cgitb
import json

from db import DB

cgitb.enable()

print('Content-type: text/html; charset=UTF-8')
print('')

db = DB('localhost', 'root', '', 'tarea2', 'utf8')

actividades = db.get_activities()

with open('./scripts/comunas.json') as coordenadas:
    geo = json.load(coordenadas)

data = []

for act in actividades:
    row = []
    id_act = act[0]
    fotos = db.get_images(id_act, False)  # lista con las fotos (solo rutas)
    comuna_id = act[1]
    comuna = db.get_comuna(comuna_id)[0][0]
    sector = act[2]
    dia_inicio = act[6].strftime('%Y-%m-%d')
    tema_id = act[9]
    row.append(dia_inicio)
    row.append(db.get_temas(tema_id)[0][0])
    row.append(sector)
    row.append(fotos)
    for coord in geo:
        if coord['name'] == comuna:
            xy = (coord['lat'], coord['lng'])
            row.append(xy)
    row.append(id_act)
    row.append(comuna_id)
    data.append(row)

# row = ["fecha inicio", "tema", "sector", [(ruta1), (ruta2), ...], (lat,long), id_act, id_comuna]
print(json.dumps(data))
