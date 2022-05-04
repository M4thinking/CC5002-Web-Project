# -*- coding: utf-8 -*-
import sys
import cgi
from db import DB
import cgitb
cgitb.enable()

print("Content-type: text/html; charset=UTF-8\r\n\r\n")
print()
sys.stdout.reconfigure(encoding='utf-8')

# db = DB("localhost", "cc500270_u", "ibuspellen", "cc500270_db", 'utf8')
db = DB('localhost', 'root', '', 'tarea2', 'utf8')

data = db.get_data()  # retorna una lista de tuplas formato (nombre, experiencia, especialidad, email,celular,path)

act = open('html/activities.html', mode="r", encoding="utf-8").read()

row_index = 0
table = "<tbody>"

for row in data:
    table += '<tr class="fila-tabla" onclick="showEventInfoPy(' + str(row[9]) + ')">'
    current_row = row
    col_index = 1
    for val in current_row:
        if col_index >= 7:
            photos = db.get_images(current_row[-1])  # Fotos según id de actividad
            table += "<td>" + str(len(photos)) + "</td>"
            break

        table += "<td>"
        table += str(val)
        table += "</td>"
        col_index = col_index + 1

    table += "</tr>"
    row_index = row_index + 1

table += """
        <script>
            let options = {
                numberPerPage: 5,
                pageCounter: true
            };
            paginate.init('.content', options);
        </script>
        """

meta = """
            <script src="../scripts/paginate.js"></script>
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

act2 = act.format(content=table)

with open('templates/template.html', mode="r", encoding="utf-8") as template:
    file = template.read()
    print(file.format(meta, 'U-Friends', act2))
