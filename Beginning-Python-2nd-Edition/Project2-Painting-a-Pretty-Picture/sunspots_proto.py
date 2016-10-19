#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import urlopen
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.lineplots import LinePlot

# data = [
#     # YR MO   PREDICTED    HIGH    LOW
#     #------------------------------------
#     (2016, 04,     29.5,    30.5,    28.5),
#     (2016, 05,     29.4,    31.4,    27.4),
#     (2016, 06,     29.3,    32.3,    26.3),
#     (2016, 07,     29.2,    34.2,    24.2),
#     (2016, 8, 29.0, 34.0, 24.0),
#     (2016, 9,     28.8,    34.8,    22.8),
#     (2016, 10,     29.0,    36.0,    22.0),
#     (2016, 11,     29.1,    36.1,    22.1),
#     (2016, 12,     29.5,    37.5,    21.5),
#     (2017, 01,     30.3,    39.3,    21.3),
#     (2017, 02,     30.2,    39.2,    21.2),
#     (2017, 03,     29.7,    39.7,    19.7),
#     (2017, 04,     28.9,    38.9,    18.9),
#     (2017, 05,     27.4,    37.4,    17.4),
#     (2017, 06,     26.1,    36.1,    16.1),
#     (2017, 07,     24.9,    34.9,    14.9),
#     (2017, 8,     23.7,    33.7,    13.7),
#     (2017, 9,     22.5,    32.5,    12.5),
#     (2017, 10,     21.4,    31.4,    11.4),
#     (2017, 11,     20.3,    30.3,    10.3),
#     (2017, 12,     19.2,    29.2,     9.2),
# ]
URL = 'http://services.swpc.noaa.gov/text/predicted-sunspot-radio-flux.txt'
COMMENT_CHARS = '#:'

drawing = Drawing(400, 200)
data = []
for line in urlopen(URL).readlines():
    if not line.isspace() and not line[0] in COMMENT_CHARS:
        data.append([float(n) for n in line.split()])

pred = [row[2] for row in data]
high = [row[3] for row in data]
low = [row[4] for row in data]
times = [row[0] + row[1]/12.0 for row in data]

lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [zip(times, pred), zip(times, high), zip(times, low)]
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

drawing.add(lp)
drawing.add(String(200, 150, 'Sunspots', fontSize=18, fillColor=colors.red, textAnchor='middle'))

renderPDF.drawToFile(drawing, 'report2.pdf', 'Sunspots')