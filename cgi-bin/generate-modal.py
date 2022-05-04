# -*- coding: utf-8 -*-
import sys
import cgi
from db import DB

print("Content-type: text/html; charset=UTF-8\r\n\r\n")
print()
sys.stdout.reconfigure(encoding='utf-8')

fs = cgi.FieldStorage()
id_act = fs['id'].value
# db = DB("localhost", "cc500270_u", "ibuspellen", "cc500270_db", 'utf8')
db = DB('localhost', 'root', '', 'tarea2', 'utf8')
data = db.get_activity(id_act)
photos = db.get_images(id_act)
if not isinstance(photos, list):
    photos = [photos]
modal_images = ''

for i in range(0, len(photos)):
    modal_images += '<img class="modal-imagen" src="../' + str(photos[i][1])
    modal_images += '" alt="' + photos[i][2] + '." onclick="abrirImagen(\'' + photos[i][1] + '\')">'

modal = f"""<div class="modal-content">
        <header class="modal-header">
        <span class="close" onclick="cerrar('modal')">x</span></header>
        <b>Información del evento</b>
        <div id="contenido-externo" class="modal-cuerpo">
            <b>Inicio: </b>{data[0][0]}
            <br><b>Término:</b> {data[0][1]}
            <br><b>Comuna:</b> {data[0][2]}
            <br><b>Sector:</b> {data[0][3]}
            <br><b>Tema: </b>{data[0][4]}
            <br><b>Nombre del Organizador: </b>{data[0][5]}
            <br><b>Fotos: </b><br> {modal_images}
        </div>
        <button id="modal-exit" onclick="cerrar('modal')">Salir</button>
        </div>
"""

js = """
    <script src="../scripts/listaActividades.js"></script>
"""
print(modal+js)
