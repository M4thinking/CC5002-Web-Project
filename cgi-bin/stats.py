# -*- coding: utf-8 -*-
import sys
from db import DB

print("Content-type: text/html; charset=UTF-8\r\n\r\n")
print()
sys.stdout.reconfigure(encoding='utf-8')

# db = DB('localhost', 'root', '', 'ejercicio4', 'utf8')
# data = db.get_data()  # retorna una lista de tuplas formato (nombre, experiencia, especialidad, email,celular,path)
stats = open('estadísticas.html', mode="r", encoding="utf-8").read()

with open('templates/template.html', mode="r", encoding="utf-8") as template:
    file = template.read()
    print(file.format('U-Friends', stats))