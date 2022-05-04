# -*- coding: utf-8 -*-
import sys
import cgi
from db import DB

print("Content-type: text/html; charset=UTF-8\r\n\r\n")
print()
sys.stdout.reconfigure(encoding='utf-8')

# db = DB("localhost", "cc500270_u", "ibuspellen", "cc500270_db", 'utf8')
db = DB('localhost', 'root', '', 'tarea2', 'utf8')

data = db.get_last_5()  # retorna una lista de 5 tuplas formato (id, nombre, sector, nombre, email, celular,
# dia_hora_inicio, dia_hora_termino, descripcion, tema)

index = open('html/inicio.html', mode="r", encoding="utf-8").read()

row_index = 0

table = ""

for row in data:
    table += '<tr class="fila-tabla" onclick="showEventInfo(' + str(row_index) + ')">'
    current_row = row
    col_index = 1
    for val in current_row:
        if col_index >= 6:
            photos = db.get_images(current_row[-1])  # Fotos según id de actividad
            table += '<td class="contenedor-imagen">'
            table += '<img class="imagen-tabla" src="../' + photos[0][1] + '" alt="Imagen principal actividad" />'
            table += "</td>"
            break

        table += "<td>"
        table += str(val)
        table += "</td>"
        col_index = col_index + 1
    table += "</tr>"
    row_index = row_index + 1

index2 = index.format(table)

with open('templates/template.html', mode="r", encoding="utf-8") as template:
    file = template.read()
print(file.format('', 'U-Friends', index2))
