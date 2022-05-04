# -*- coding: utf-8 -*-
import sys
import cgi
import cgitb
cgitb.enable()

print("Content-type: text/html; charset=UTF-8\r\n\r\n")
print()
sys.stdout.reconfigure(encoding='utf-8')

form = open('html/form.html', mode="r", encoding="utf-8").read()

with open('templates/template.html', mode="r", encoding="utf-8") as template:
    file = template.read()
    print(file.format('', 'U-Friends', form))
