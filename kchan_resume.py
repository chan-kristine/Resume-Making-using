import os as access
from fpdf import FPDF


 # Important Values
User = 'KRISTINE AGCAY CHAN' 
file_name = 'CHAN_Kristine.pdf' 
char = 'Personal Details'
json_file = "resume.json" 

class PDF(FPDF):
# setting the header
    def header(self): 
        self.image('header.png', 170, 0, 40, 0) 
        self.image('me.png', 10, 0, 50, 0) 
        self.set_font('helvetica', 'B', 25) 
        self.cell(180, 35, User, ln = 1, align = 'R'); 
        self.cell(90, 20, char) 
        self.ln(10)

# setting the data
    def json_body(self, name):
        with open(json_file) as fh: 
            chr = fh.read() 
        self.set_font("helvetica", "", 11)
        self.multi_cell(0, 4, chr)

# setting the page 
    def print_chap(self, num, title, name): 
        self.add_page()
        self.json_body(name)


# PDF maker
Kchanpdf = PDF('P', 'mm', 'A4') 
Kchanpdf.set_auto_page_break(margin = 0.5, auto = True) 
Kchanpdf.print_chap(1, "", json_file)
Kchanpdf.output(file_name)
# Open the file 
access.startfile(file_name)