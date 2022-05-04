# -*- coding: utf-8 -*-
import cgi
import os
import sys
import filetype
import html
import re

from db import DB
from datetime import datetime

print("Content-type: text/html; charset=UTF-8\r\n\r\n")
print()
sys.stdout.reconfigure(encoding='utf-8')

# Establecemos conexion con la base de datos
# db = DB("3306,", "cc500270_u", "ibuspellen", "cc500270_db")
db = DB('localhost', 'root', '', 'tarea2', 'utf8')

form = cgi.FieldStorage()
photos = form['foto-actividad']

# VALIDACIÓN LADO SERVIDOR
err = ""  # Error base

# Validation region y comuna
id_region_comuna = [{"idComunas": ["10301", "10302", "10303", "10304", "10305", "10306", "10307"]},
                    {
                        "idComunas": ["20101", "20102", "20201", "20202", "20203", "20301", "20302", "20303", "20304"]},
                    {
                        "idComunas": ["30101", "30102", "30201", "30202", "30203", "30301", "30302", "30303", "30304"]},
                    {
                        "idComunas": ["40101", "40102", "40103", "40104", "40105", "40106", "40201", "40202", "40203",
                                      "40204", "40205", "40301", "40302", "40303", "40304"]}, {
                        "idComunas": ["50101",
                                      "50102",
                                      "50103",
                                      "50104",
                                      "50105",
                                      "50201",
                                      "50202",
                                      "50203",
                                      "50204",
                                      "50205",
                                      "50206",
                                      "50301",
                                      "50302",
                                      "50303",
                                      "50304",
                                      "50305",
                                      "50306",
                                      "50307",
                                      "50401",
                                      "50402",
                                      "50403",
                                      "50404",
                                      "50501",
                                      "50502",
                                      "50503",
                                      "50504",
                                      "50505",
                                      "50506",
                                      "50507",
                                      "50508",
                                      "50509",
                                      "50601",
                                      "50701",
                                      "50702",
                                      "50703",
                                      "50704",
                                      "50705",
                                      "50706"]},
                    {
                        "idComunas": ["60101", "60102", "60103", "60104", "60105", "60106", "60107", "60108", "60109",
                                      "60110", "60111", "60112", "60113", "60114", "60115", "60116", "60117", "60201",
                                      "60202", "60203", "60204", "60205", "60206", "60301", "60302", "60303", "60304",
                                      "60305", "60306", "60307", "60308", "60309", "60310"]}, {
                        "idComunas": ["70101",
                                      "70102",
                                      "70103",
                                      "70104",
                                      "70105",
                                      "70106",
                                      "70107",
                                      "70108",
                                      "70109",
                                      "70201",
                                      "70202",
                                      "70203",
                                      "70204",
                                      "70205",
                                      "70206",
                                      "70207",
                                      "70208",
                                      "70209",
                                      "70210",
                                      "70301",
                                      "70302",
                                      "70303",
                                      "70304",
                                      "70305",
                                      "70306",
                                      "70307",
                                      "70308",
                                      "70401",
                                      "70402",
                                      "70403"]},
                    {
                        "idComunas": ["80201", "80202", "80203", "80204", "80205", "80206", "80207", "80208", "80209",
                                      "80210", "80211", "80212", "80301", "80302", "80303", "80304", "80305", "80306",
                                      "80307", "80308", "80309", "80310", "80311", "80312", "80313", "80314", "80401",
                                      "80402", "80403", "80404", "80405", "80406", "80407"]}, {
                        "idComunas": ["90101",
                                      "90102",
                                      "90103",
                                      "90104",
                                      "90105",
                                      "90106",
                                      "90107",
                                      "90108",
                                      "90109",
                                      "90110",
                                      "90111",
                                      "90201",
                                      "90202",
                                      "90203",
                                      "90204",
                                      "90205",
                                      "90206",
                                      "90207",
                                      "90208",
                                      "90209",
                                      "90210",
                                      "90211",
                                      "90212",
                                      "90213",
                                      "90214",
                                      "90215",
                                      "90216",
                                      "90217",
                                      "90218",
                                      "90219",
                                      "90220",
                                      "90221"]},
                    {
                        "idComunas": ["100201", "100202", "100203", "100204", "100205", "100206", "100207", "100301",
                                      "100302", "100303", "100304", "100305", "100306", "100307", "100308", "100309",
                                      "100401", "100402", "100403", "100404", "100405", "100406", "100407", "100408",
                                      "100409", "100410", "100501", "100502", "100503", "100504"]}, {
                        "idComunas": [
                            "110101",
                            "110102",
                            "110103",
                            "110201",
                            "110202",
                            "110301",
                            "110302",
                            "110401",
                            "110402",
                            "110403"]},
                    {
                        "idComunas": ["120101", "120102", "120201", "120202", "120203", "120204", "120301", "120302",
                                      "120303", "120401"]}, {
                        "idComunas": ["130101", "130102", "130103", "130201",
                                      "130202",
                                      "130203", "130204", "130205", "130206",
                                      "130207",
                                      "130208", "130209", "130210", "130211",
                                      "130212",
                                      "130213", "130214", "130215", "130216",
                                      "130217",
                                      "130218", "130219", "130220", "130221",
                                      "130222",
                                      "130223", "130224", "130225", "130226",
                                      "130227",
                                      "130228", "130229", "130230", "130231",
                                      "130232",
                                      "130301", "130302", "130303", "130401",
                                      "130402",
                                      "130403", "130404", "130501", "130502",
                                      "130503",
                                      "130504", "130601", "130602", "130603",
                                      "130604",
                                      "130605", "130606"]}, {
                        "idComunas": ["100101",
                                      "100102",
                                      "100103",
                                      "100104",
                                      "100105",
                                      "100106",
                                      "100107",
                                      "100108",
                                      "100109",
                                      "100110",
                                      "100111",
                                      "100112"]},
                    {"idComunas": ["10101", "10102", "10201", "10202"]}, {
                        "idComunas": ["80101",
                                      "80102",
                                      "80103",
                                      "80104",
                                      "80105",
                                      "80106",
                                      "80107",
                                      "80108",
                                      "80109",
                                      "80110",
                                      "80111",
                                      "80112",
                                      "80113",
                                      "80114",
                                      "80115",
                                      "80116",
                                      "80117",
                                      "80118",
                                      "80119",
                                      "80120",
                                      "80121"]}]

region = int(html.escape(form['region'].value))
if not (1 <= region <= 16):
    err += "Error en la región ingresada. Por favor, rellene nuevamente el formulario.\n"

comuna = html.escape(form['comuna'].value, quote= True)

if comuna not in id_region_comuna[region-1]["idComunas"]:
    err += "Error en la comuna ingresada. Por favor, rellene nuevamente el formulario.\n"

# Validar sector
sector = html.escape(form['sector'].value)
if not (sector == "" or len(sector) <= 100):
    err += "El nombre de sector ingresado es muy largo. Por favor rellene nuevamente el formulario.\n"

# Validar nombre
nombre = html.escape(form['nombre'].value, quote=True)
if not (0 < len(nombre) < 200):
    err += "El nombre de contacto ingresado es muy largo, o muy corto. Por favor rellene nuevamente el formulario.\n"

# Validar email
email = html.escape(form['email'].value, quote=True)
r_email = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b'

if (re.fullmatch(r_email, email)) is None:
    err += "Error en el email ingresado. Por favor, rellene nuevamente el formulario.\n"

# Validar celular (opcional)
r_celular = r'\b\D*([+56]\d [2-9])(\D)(\d{4})(\D)(\d{4})\D*\b'
celular = html.escape(form['celular'].value, quote=True)

if (re.fullmatch(r_celular, celular)) or celular == "":
    err += "Teléfono celular ingresado no cumple con el estándar telefónico chileno.\n"

# Validar redes sociales/de contacto

# Validador tipo de URLs
url_regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,14}\.\d{1,14}\.\d{1,14}\.\d{1,14})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

# Se guardan las redes sociales del formulario
contact = form['contactar-por']
wa = html.escape(contact[0].value, quote=True)
tg = html.escape(contact[1].value, quote=True)
tw = html.escape(contact[2].value, quote=True)
ig = html.escape(contact[3].value, quote=True)
fb = html.escape(contact[4].value, quote=True)
tk = html.escape(contact[5].value, quote=True)
ot = html.escape(contact[6].value, quote=True)

# Whatsapp
if wa != '':  # si se relleno el input de whatsapp
    url_default = "https://wa.me/"
    if not (4 <= len(wa) <= 50):
        err += "Error con el formato de 'Whatsapp', red social debe estar entre 4 y 50 caracteres.\n"
    if wa.find('+') != -1 and wa.find('wa.me') == -1:  # Si es un número de teléfono y no tiene escrito la url
        wa = wa.replace('+', '')
        wa = wa.replace(' ', '')
        url = url_default + wa
        if re.match(url_regex, url) is None:
            err += "Error con el formato de su usuario de Whatsapp. Por favor, agregue un + antes de su contacto (Ej: " \
                  "+39 334 840 492).\n"
    else:  # Solo puede ser URL
        if re.match(url_regex, wa) is None:
            err += "Error con el formato de su URL al perfil de Whatsapp. Por favor, ingrese un URL válido.\n"

# Twitter
if tw != '':  # si se relleno el input de twitter
    url_default = "https://www.twitter.com/"
    if not (4 <= len(tw) <= 50):
        err += "Error con el formato de 'Twitter', red social debe estar entre 4 y 50 caracteres.\n"
    elif tw.find('@') != -1 and tw.find('twitter') == -1:  # Si es un usuario y no tiene escrito la url
        tw = tw.replace('@', '')
        url = url_default + tw
        if re.match(url_regex, url) is None:
            err += "Error con el formato de su usuario de Twitter. Por favor, agregue un @ antes de su usuario (Ej: " \
                  "@nombre_usuario\n"
    else:  # Solo puede ser URL
        if re.match(url_regex, tw) is None:
            err += "Error con el formato de su URL al perfil de Twitter. Por favor, ingrese un URL válido.\n"

# Telegram
if tg != '':  # Si se relleno el input de telegram
    url_default = "https://web.telegram.org/"
    if not (4 <= len(tg) <= 50):
        err += "Error con el formato de 'Telegram', red social debe estar entre 4 y 50 caracteres.\n"
    elif tg.find('@') != -1 and tg.find('telegram') == -1:  # Si es un usuario y no tiene escrito la url
        tg = tg.replace('@', '')
        url = url_default + tg
        if re.match(url_regex, url) is None:
            err += "Error con el formato de su usuario de Telegram. Por favor, agregue un @ antes de su usuario (" \
                  "Ej: @nombre_usuario).\n"
    else:  # Solo puede ser URL
        if re.match(url_regex, tg) is None:
            err += "Error con el formato de su URL al perfil de Telegram. Por favor, ingrese un URL válido.\n"

# Instagram
if ig != '':  # Si se relleno el input de instagram
    url_default = "https://www.instagram.com/"
    if not (4 <= len(ig) <= 50):
        err += "Error con el formato de 'Instagram', red social debe estar entre 4 y 50 caracteres.\n"
    elif ig.find('@') != -1 and ig.find('instagram') == -1:  # Si es un usuario y no tiene escrito la url
        ig = ig.replace('@', '')
        url = url_default + ig
        if re.match(url_regex, url) is None:
            err += "Error con el formato de su usuario de Instagram. Por favor, agregue un @ antes de su usuario (" \
                  "Ej: @nombre_usuario).\n"
    else:  # Solo puede ser URL
        if re.match(url_regex, ig) is None:
            err += "Error con el formato de su URL al perfil de Instagram. Por favor, ingrese un URL válido.\n"

# Facebook
if fb != '':  # Si se relleno el input de facebook
    url_default = "https://www.facebook.com/"
    if not (4 <= len(fb) <= 50):
        err += "Error con el formato de 'Facebook', red social debe estar entre 4 y 50 caracteres.\n"
    elif fb.find('@') != -1 and fb.find('facebook') == -1:  # Si es un usuario y no tiene escrito la url
        fb = fb.replace('@', '')
        url = url_default + fb
        if re.match(url_regex, url) is None:
            err += "Error con el formato de su usuario de Facebook. Por favor, agregue un @ antes de su usuario (Ej: " \
                  "@nombre_usuario).\n"
    else:  # Solo puede ser URL
        if re.match(url_regex, fb) is None:
            err += "Error con el formato de su URL al perfil de Facebook. Por favor, ingrese un URL válido.\n"

# Tik Tok
if tk != '':  # Si se relleno el input de tiktok
    url_default = "https://www.tiktok.com/"
    if not (4 <= len(tk) <= 50):
        err += "Error con el formato de 'Tik Tok', red social debe estar entre 4 y 50 caracteres.\n"
    elif tk.find('@') != -1 and tk.find('tiktok') == -1:  # Si es un usuario y no tiene escrito la url
        tk = tk.replace('@', '')
        url = url_default + tk
        if re.match(url_regex, url) is None:
            err += "Error con el formato de su usuario de TikTok. Por favor, agregue un @ antes de su usuario (Ej: " \
                  "@nombre_usuario).\n"
    else:  # Solo puede ser URL
        if re.match(url_regex, tk) is None:
            err += "Error con el formato de su URL al perfil de TikTok. Por favor, ingrese un URL válido.\n"

# Otra
if ot != '':
    if not (3 <= len(ot) <= 15):
        err += "Error con el formato de 'Otra red social', red social debe estar entre 3 y 15 caracteres.\n"
    elif ot.find('@') != -1 or ot.find('+') != -1:  # Si se ingreso un nombre de usuario o un numero de telefono extra
        err += "Error con el formato de 'Otra red social'. Por favor, ingrese una URL válida a su perfil. No ingrese " \
              "un usuario o numero.\n"
    else:
        if re.match(url_regex, ot) is None:
            err += "Error con el formato de 'Otra red social'. Por favor, ingrese una URL válida a su perfil.\n"


# Fecha de inicio y término
dia_hora_inicio = html.escape(form['dia-hora-inicio'].value, quote=True)
dia_hora_termino = html.escape(form['dia-hora-termino'].value, quote=True)

try:
    datetime.strptime(dia_hora_inicio, "%Y-%m-%d %H:%M")
except ValueError:
    err += "Error con la fecha de inicio del evento. Por favor, rellene nuevamente el formulario.\n"

try:
    datetime.strptime(dia_hora_termino, "%Y-%m-%d %H:%M")
except ValueError:
    err += "Error con la fecha de término del evento. Por favor, rellene nuevamente el formulario.\n"

# Validar descripción
descripcion = html.escape(form['descripcion-evento'].value, quote=True)

# Validar tema
temas_actuales = db.get_temas()
tema = form['tema']
otro_tema = ""

if not isinstance(tema, list): # Se elige un tema de la bd o no lo ingresa
    tema_id = html.escape(form['tema'].value, quote=True)
    if (tema_id == ''):
        err += "Error en el tema ingresado, ingresa un tema.\n"
    else:
        tema_id = int(html.escape(form['tema'].value, quote=True))
        if not (temas_actuales[0][0] <= int(tema_id) <= temas_actuales[-1][0]):
            err += "Error en el tema ingresado, ingresa un tema válido.\n"
else:  # Se elige otro tema asociado a un nuevo input [id, nombre]
    tema_id = int(html.escape(form['tema'][0].value, quote=True))
    otro_tema = html.escape(form['tema'][1].value, quote=True)
    if not (3 <= len(otro_tema) <= 15 and tema_id == (temas_actuales[-1][0]+1) ):
        err += "Error en el tema ingresado, ingresa un tema con entre 3 y 15 caracteres.\n"

MAX_FILE_SIZE = 100*1000000 # 100 MB

if not isinstance(photos, list):
    photos = [photos]
if not isinstance(contact, list):
    contact = [contact]

for photo in photos:
    if photo.filename:
        tipo = photo.type
        size = os.fstat(photo.file.fileno()).st_size
        photo_type = filetype.guess(photo.file)
        photo.file.seek(0, 0)
        if (photo_type.mime != 'image/jpeg') and (photo_type.mime != 'image/png') and (photo_type.mime != 'image/jpg'):
            err += "Una de sus fotos no corresponde al tipo correcto. Por favor, cerciórese de que estos sean de tipo JPG, JPEG o PNG.\n"
        if size > MAX_FILE_SIZE:
            err += "Una de sus fotos pesa demasiado. Por favor, verifique que el peso de cada archivo no sea mayor a 100MB.\n"
    else:
        err += "Error, foto no subida. Por favor, verifique la correcta subida de archivos.\n"

activity = (comuna, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion, tema_id, otro_tema)

if err != "":  # Si hubo errores
    # https://anakena.dcc.uchile.cl/~cc500216/cgi-bin/form.py
    print(f"""
        <div class="warn">
            <span class="closebtn black" onclick="this.parentElement.style.display=\'none\';">&times;</span>
            Se encontraron los siguientes errores:\n{err}
        </div>
    """)
    # meta = '''
    #     <meta http-equiv="refresh" content="50; url='form.py'">
    # '''
    #
    # title = 'Estas siendo redirigido...'
    #
    # content = f"""
    #     <div class='contenido'>
    #     <p> Su formulario ha fallado en: " {err} "</p>"
    #     <p> Si no ha sido redirigido en 50seg. haga click <a href='form.py'>aquí</a> </p>
    #     </div>
    # """
    # with open('templates/template.html', mode="r", encoding="utf-8") as template:
    #     file = template.read()
    #     print(file.format(meta, title, content))

else: # No hay errores, se aplica la conexión

    db = DB('localhost', 'root', '', 'tarea2', 'utf8')
    db.save_data(activity,contact, photos) # insertamos la informacion en la base
    head = f"""
            <meta http-equiv="refresh" content="5;url='index.py'">
        """

    title = "Estas siendo redirigido..."
    message = """
            <div id="mensaje-envío" class="contenido">
                        <p> Hemos recibido su información, muchas gracias y suerte en su actividad.</p>
                        <a class="link-button" href="index.py">Volver al Inicio</a>
            </div>
    """

    with open('templates/template.html', mode="r", encoding="utf-8") as template:
        file = template.read()
        print(file.format(head, title, message))
