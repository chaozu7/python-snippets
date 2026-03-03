from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("shirtificate.png", 15, 65, 180)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", style="B", size=25)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(40, 10, "CS50 Shirtificate", align="C")


def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.add_page(orientation="P", format="A4")
    pdf.set_font('helvetica', size=27)
    pdf.set_text_color(255,255,255)
    pdf.cell(-40,250, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")



if __name__ == "__main__":
    main()


