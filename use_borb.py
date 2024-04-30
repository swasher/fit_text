from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import SingleColumnLayout
from borb.pdf import Paragraph
from borb.pdf import PDF
from util import mm
from decimal import Decimal


def use_borb(txt, w, h):
    h *= mm
    w *= mm

    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page(w, h)

    # add Page to Document
    doc.add_page(page)

    horizontal_margin = page.get_page_info().get_width() * Decimal(0.5)
    vertical_margin = page.get_page_info().get_height() * Decimal(0.5)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # add a Paragraph
    font_size = Decimal(45)
    exit_loop = False
    while not exit_loop:
        try:
            layout.add(Paragraph(txt, font='Helvetica', font_size=font_size, fixed_leading=Decimal(1)))
            exit_loop = True
        except AssertionError:
            font_size -= Decimal(0.1)

    # store
    with open("sample_borb.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)
