import json
from fpdf import FPDF

# format - PDF
pdf = FPDF('P', 'cm', 'A4') 
pdf.add_page()

# Infos to be read
resume_info= open('resume.json', 'r')
res_maker= resume_info.read()
raw_infos= json.loads(res_maker)
