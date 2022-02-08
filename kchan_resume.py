import os as access
from ctypes import alignment
import json
from fpdf import FPDF


#READ INFOS
res_info= open('resume.json', 'r')
res_maker= res_info.read()
raw_infos= json.loads(res_maker)


# SETTING HEADER
class PDF(FPDF):
    def header(self):  
        self.image('me.jpg', 10, 8,40) 
        self.set_font('helvetica', 'B', 28.5) 
        self.cell(0, 30, 'KRISTINE AGCAY CHAN', ln = 1, align = 'R'); 
        self.ln(3)

#PDFFormat
pdf = PDF('P', 'mm', 'Letter') 
pdf.add_page()


# DATA
for user_info in raw_infos:
    pdf.ln(5)
    pdf.set_font('helvetica', 'BI', 18)
    pdf.cell(0, 10, f"{user_info['title1']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('helvetica', '' , 12)
    pdf.cell(0,5, f"Name: {user_info['name']}",align="L", ln=1)
    pdf.cell(0,5, f"Email Address: {user_info['emailadd']}",align="L",ln=1)
    pdf.cell(0,5, f"Address: {user_info['address']}",align="L",ln=1)
    pdf.cell(0,5, f"Contact Number: {user_info['contactnumber']}", align="L", ln=1)
    pdf.ln(8)
    pdf.set_font('helvetica', 'BI', 18)
    pdf.cell(0, 10, f"{user_info['title2']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('helvetica', '' , 12)
    pdf.cell(0, 10, f"{user_info['objectives']}", 'BI', ln=1)
    pdf.ln(8)
    pdf.set_font('helvetica', 'BI', 18)
    pdf.cell(0, 10, f"{user_info['title3']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('helvetica', 'BIU', 12)
    pdf.cell(0, 5, f"{user_info['tertiarylvl']}", align='L', ln=1)
    pdf.set_font('helvetica', 'I', 12)
    pdf.cell(0, 5, f"{user_info['tschooladd']}", align='L', ln=1)
    pdf.set_font('helvetica', 'I', 12)
    pdf.ln(3)
    pdf.set_font('helvetica', 'BIU', 12)
    pdf.cell(0, 5, f"{user_info['secondlvl']}", align='L', ln=1)
    pdf.set_font('helvetica', 'I', 12)
    pdf.cell(0, 5, f"{user_info['sschooladd']}", align='L', ln=1)
    pdf.set_font('helvetica', 'I', 12)
    pdf.ln(3)
    pdf.set_font('helvetica', 'BIU', 12)
    pdf.cell(0, 5, f"{user_info['primlvl']}", align='L', ln=1)
    pdf.set_font('helvetica', 'I', 12)
    pdf.cell(0, 5, f"{user_info['pschooladd']}", align='L', ln=1)
    pdf.set_font('helvetica', 'BI', 12)
    pdf.ln(8)
    pdf.set_font('helvetica', 'BI', 18)
    pdf.cell(0, 10, f"{user_info['title4']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('helvetica', 'I', 12)
    pdf.cell(0, 5, f"{user_info['Skll1']}", align='L', ln=1)
    pdf.cell(0, 5, f"{user_info['Skll2']}", align='L', ln=1)
    pdf.cell(0, 5, f"{user_info['Skll3']}", align='L', ln=1)
    pdf.set_font('helvetica', 'BI', 18)
    pdf.ln(8)
    pdf.cell(0, 10, f"{user_info['title5']}", 'BI', ln=1)
    pdf.set_font('helvetica', 'I', 12)
    pdf.cell(0, 5, f"{user_info['achieve1']}", align='L', ln=1)
    pdf.cell(0, 5, f"{user_info['achieve2']}", align='L', ln=1)
    pdf.cell(0, 5, f"{user_info['achieve3']}", align='L', ln=1)
    pdf.cell(0, 5, f"{user_info['achieve4']}", align='L', ln=1)
    pdf.cell(0, 5, f"{user_info['achieve5']}", align='L', ln=1)
    pdf.cell(0, 5, f"{user_info['achieve6']}", align='L', ln=1)
 


#PDF MAKER
pdf.output('CHAN_Kristine.pdf')
#FILE OPENER
access.startfile('CHAN_Kristine.pdf')