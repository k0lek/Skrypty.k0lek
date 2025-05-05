from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

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
styles = getSampleStyleSheet()
report_title = Paragraph("A complete inventory of my fruit", styles["h1"])
table_data = []
table_style = [('GRID', (0,0), (-1, -1), 1, colors.black)]
for k,v in fruit.items():
  table_data.append([k, v])
print(table_data)
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
report.build([report_title, report_table])

"""#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(attachment, file, pharagraph):
  styles = getSampleStyleSheet() 
  report = SimpleDocTemplate(attachment)
  report_title = Paragraph(title, styles['h1'])
  report_info = Paragraph(paragraph, styles['BodyText'])
  table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black),    
                 ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  
                 ('ALIGN', (0, 0), (-1, -1), 'CENTER')]  
  empty_line = Spacer(1, 20)
  report.build([report_title, empty_line, report_info])"""
