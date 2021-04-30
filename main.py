from fpdf import FPDF
from bill import *


class PDF(FPDF):
    def header(self):
        self.image('logo.png', 10, 8, 40)
        self.ln(50)

    def footer(self):

        self.image('bar.jpg', 30, 175, 50)
        self.ln(40)
        self.image('awb.PNG', 20, 220, 80)


pdf = PDF('P', 'mm', 'Letter')

pdf.add_page()

pdf.set_font('helvetica', '', 14)
pdf.cell(110, 10, "DELIVER TO:", ln=0)
pdf.cell(0, 10, "SHIPPED BY:", ln=1)
pdf.cell(110)
pdf.set_font('helvetica', 'B', 14)
pdf.cell(0, 10, str(package_details['shipping_address']), ln=1)

pdf.set_font('helvetica', 'B', 12)
for i in user_details:
    pdf.cell(55, 10, str(user_details[i]), ln=1)

pdf.cell(55, 30, " ", ln=1)
pdf.set_font('helvetica', '', 12)
pdf.cell(20)
pdf.cell(15, 5, "ORDER#: ", ln=0)
pdf.cell(5, 5, str(package_details['package_ID']), ln=1)

pdf.cell(40, 50, " ", ln=1)
pdf.cell(20)
pdf.cell(15, 5, "AWB#: ", ln=0)
pdf.cell(5, 5, str(AWB), ln=1)

print("Label Generated Successfully!!!")
pdf.output('label.pdf')
