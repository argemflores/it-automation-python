#!/usr/bin/env python3

# Import Page Layout and Typography Using Scripts (PLATYPUS)
from reportlab.platypus import SimpleDocTemplate

fruit = {
    "elderberries": 1,
    "figs": 1,
    "apples": 2,
    "durians": 3,
    "bananas": 5,
    "cherries": 8,
    "grapes": 13
}

report = SimpleDocTemplate('report.pdf')

# Import Flowables, like chunks of a document that reportlab can arrange to make a complete report
from reportlab.platypus import Paragraph, Spacer, Table, Image

# Import style for each part of the document
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()

# Make the report title using the H1 style
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

# Build the PDF document using the list of Flowable elements
# report.build([report_title]) # generates report.pdf

##########

# Convert a dictionary to a list of lists
table_data = []
for k, v in fruit.items():
    table_data.append([k, v])
# print(table_data) # prints: ['elderberries', 1], ['figs', 1], ['apples', 2], ['durians', 3], ['bananas', 5], ['cherries', 8], ['grapes', 13]]

# Create table and add it to report
report_table = Table(data=table_data)
# report.build([report_title, report_table]) # generates report.pdf

# Add styles to table: border around cells, left-justified
from reportlab.lib import colors

table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
# report.build([report_title, report_table]) # generates report.pdf

##########

# Create a Pie object
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.pagesizes import inch

# Create a Pie object with width and height set to 3 inches
report_pie = Pie(width=3*inch, height=3*inch)

# Create data and labels lists for the Pie object
report_pie.data = []
report_pie.labels = []

# Sort the fruit in alphabetical order
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

# print(report_pie.data) # prints: [2, 5, 8, 3, 1, 1, 13]
# print(report_pie.labels) # prints: ['apples', 'bananas', 'cherries', 'durians', 'elderberries', 'figs', 'grapes']

# Place Pie object inside a Flowable Drawing
report_chart = Drawing()
report_chart.add(report_pie)

# Build the PDF document with the new Drawing
report.build([report_title, report_table, report_chart])
