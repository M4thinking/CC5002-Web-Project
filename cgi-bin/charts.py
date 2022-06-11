# -*- coding: utf-8 -*-
import cgi
import cgitb
import json

from db import DB

cgitb.enable()

print('Content-type: text/html; charset=UTF-8')
print('')

form = cgi.FieldStorage()
# print(form, "\n")

if 'tipo' in form:

    tipo = form.getvalue('tipo')

    # Abrimos una conexion a la base de datos

    db = DB('localhost', 'root', '', 'tarea2', 'utf8')

    if tipo == 'eventosxdia':
        data = db.events_per_day()  # obtenemos la información de la consulta

    elif tipo == 'torta':
        data = db.count_type()

    elif tipo == 'barras':
        data = db.events_per_hour()

    rows = {}
    k = 0
    for d in data:
        rows[k] = list(d)  # diccionario con listas como valores
        k += 1

    print(json.dumps(rows))  # devolvemos como un archivo json

else:
    print("Error con el formulario \n")
