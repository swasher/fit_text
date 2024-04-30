from fpdf import FPDF


def use_fpdf(txt, w, h, margins):

    font_size = 3
    overflow = False

    while not overflow:
        font_size += 1
        pdf = FPDF()
        pdf.add_page(format=(w, h))
        pdf.set_margin(margins)

        pdf.set_font('Arial', 'B', font_size)
        overflow = pdf.write(text=txt)
        # print(overflow)

    font_size -= 1
    pdf = FPDF()
    pdf.add_page(format=(w, h))
    pdf.set_margin(margins)

    pdf.set_font('Arial', 'B', font_size)
    overflow = pdf.write(text=txt)

    pdf.output('sample_fpdf.pdf', 'F')
