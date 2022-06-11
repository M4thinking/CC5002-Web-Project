# -*- coding: utf-8 -*-
import sys
import cgi
from db import DB

print("Content-type: text/html; charset=UTF-8\r\n\r\n")
print()
sys.stdout.reconfigure(encoding='utf-8')

meta = """
    <script src="https://cdn.jsdelivr.net/npm/flot-charts@0.8.3/jquery.flot.min.js"></script>
    <script src="https://code.highcharts.com/highcharts.js"></script>
    <script src="https://code.highcharts.com/modules/data.js"></script>
    <script src="https://code.highcharts.com/modules/exporting.js"></script>
    <script src="https://code.highcharts.com/modules/accessibility.js"></script>
"""

stats = open('html/estadisticas.html', mode="r", encoding="utf-8").read()

with open('templates/template.html', mode="r", encoding="utf-8") as template:
    file = template.read()
    print(file.format(meta, 'U-Friends', stats))
