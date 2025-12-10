from fpdf import FPDF

class PDF(FPDF):
    
    def _text_cell(self, text, align="L"):
        self.set_font("helvetica", size=14)
        self.set_fill_color(240, 248, 255)
        width = self.get_string_width(text) + 6
        self.set_x((210 - width) / 2)
        self.cell(width, 9, text, border=0, fill=True, align=align)
        self.ln(12) 

    def make_title(self):
        self.set_font("helvetica", style="B", size=18)
        self.set_fill_color(200, 220, 255)
        self.ln(15)
        self._text_cell(self.title)

    def make_time(self, time_str):
        self._text_cell(f"Time for cooking: {time_str}")

    def make_instructions(self, instructions):
        self.set_font("helvetica", size=12)
        self.multi_cell(0, 8, instructions)
        self.ln(10)
        
    def make_picture(self, picture_url):
        self.set_font("helvetica", size=12)
        self._text_cell(f"The picture url is: {picture_url}")
        self.ln(10)


    def prepare_pdf(self, time, instructions, picture):
        self.add_page()
        self.make_title()
        self.make_time(time)
        self.make_picture(picture)
        self.make_instructions(instructions)


def receipt(title, time, instructions, picture):
    pdf_generator = PDF(orientation="P", unit="mm", format="A4")
    pdf_generator.set_title(title)
    pdf_generator.prepare_pdf( time, instructions, picture)
    pdf_generator.output(f"{title}.pdf")