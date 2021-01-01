#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

"""Generate a report containing a title and a paragraph saved in attachment"""
def generate_report(attachment, title, paragraph):
    report = SimpleDocTemplate(attachment)

    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles['h1'])
    report_paragraph = Paragraph(paragraph)

    report.build([report_title, report_paragraph])
