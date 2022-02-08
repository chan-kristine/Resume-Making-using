import os as access
from ctypes import alignment
import json
from fpdf import FPDF

#PDF Format
pdf = FPDF('P', 'mm', 'Letter') 
pdf.add_page()


#Read Informations
res_info= open('resume.json', 'r')
res_maker= res_info.read()
raw_infos= json.loads(res_maker)
#images
class PDF(FPDF):
    def header(self): 
        self.image('me.png', 10, 8, 40) 
        self.set_font('helvetica', 'B', 28.5) 
        self.cell(0, 30,ln = 1, align = 'R'); 
        self.ln(3)

#Informations
for user_info in raw_infos:
    pdf.set_font('helvetica', 'B', 20)
    pdf.cell(0,30, f"{user_info['firstname']} {user_info['middlename']} {user_info['lastname']}", align= "R", ln=1)
    pdf.set_font('helvetica', 'BI', 18)
    pdf.cell(5,1,"Personal Info", ln=1)
    pdf.set_font('helvetica', "", 12)
    pdf.cell(0,5, f"Name: {user_info['name']}",align="L", ln=1)
    pdf.cell(0,5, f"Email Address: {user_info['emailadd']}",align="L",ln=1)
    pdf.cell(0,5, f"Address: {user_info['address']}",align="L",ln=1)
    pdf.cell(0,5, f"Contact Number: {user_info['contactnumber']}", align="L", ln=1)
    

#PDF Maker
pdf.output('CHAN_Kristine.pdf')

access.startfile('CHAN_Kristine.pdf')