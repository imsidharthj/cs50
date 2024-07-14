from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 50)
        self.cell(0, 60, "CS50 Shirtificate", align='C')

    def add_shirt_image(self, image_path):
        self.image(image_path, x=0, y=70)

    def add_shirt_text(self, user_name):
        self.set_font("helvetica", "B", 30)
        self.set_text_color(255, 255, 255)
        self.text(x=55, y=140, txt=f'{user_name} took CS50')

name = input("Name: ")
pdf = PDF(orientation="P", format="A4")
pdf.add_page()
pdf.add_shirt_image("shirtificate.png")
pdf.add_shirt_text(name)
pdf.output("shirtificate.pdf")
