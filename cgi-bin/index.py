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
# dia_hora_inicio, dia_hora_termino, descripción, tema)

index = open('html/inicio.html', mode="r", encoding="utf-8").read()

row_index = 0

table = ""

for row in data:
    table += '<tr class="fila-tabla">'
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
meta = """
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin=""/>
    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>

    <script>
        function showEventInfoPy(id_act){{
                $.ajax({
                    url: "/cgi-bin/generate-modal.py",
                    type: "post",
                    datatype:"json",
                    data: {'id': id_act},
                    success: function(response) {{
                        $('#modal-detalle').html(response);
                        document.getElementById('modal-detalle').style.display = "block";
                    }}
                })
        }}
    </script>
"""

mapa = '''
    <div id='map' class="mapa">
        <script src="../scripts/mapa.js"></script>
    </div>

'''

index2 = index.format(table, mapa)

with open('templates/template.html', mode="r", encoding="utf-8") as template:
    file = template.read()
print(file.format(meta, 'U-Friends', index2))
