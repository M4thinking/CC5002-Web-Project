# -*- coding: utf-8 -*-
import sys
import cgi
from db import DB

print("Content-type: text/html; charset=UTF-8\r\n\r\n")
print()
sys.stdout.reconfigure(encoding='utf-8')

stats = open('html/estadisticas.html', mode="r", encoding="utf-8").read()

with open('templates/template.html', mode="r", encoding="utf-8") as template:
    file = template.read()
    print(file.format('','U-Friends', stats))