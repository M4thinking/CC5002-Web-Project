# -*- coding: utf-8 -*-
import sys
import cgi
from db import DB

print("Content-type: text/html; charset=UTF-8\r\n\r\n")
print()
sys.stdout.reconfigure(encoding='utf-8')

# db = DB("localhost", "cc500270_u", "ibuspellen", "cc500270_db", 'utf8')
db = DB('localhost', 'root', '', 'tarea2', 'utf8')
temas = db.get_temas()

options = "<option value="">Selecciona una opción</option>"
for tema in temas:
    options += f'<option value="{tema[0]}" name = "tema">{tema[1]}</option>'
options += f'<option value="{temas[-1][0]+1}" name = "tema">otro</option>'

print(options)
