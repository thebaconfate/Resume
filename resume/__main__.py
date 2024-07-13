from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black
from reportlab.platypus import Frame, Paragraph
from reportlab.lib.units import inch
from resume.border import Border
from reportlab.lib.styles import getSampleStyleSheet


c = Canvas("hello.pdf")
border = Border(*A4)
print(border.min_width, border.min_height)
print(border.max_width, border.max_height)
print(border.width, border.height)

c.setFillColorRGB(37 / 255, 150 / 255, 190 / 255)
DETAILS_MIN_WIDTH = border.min_width
DETAILS_MIN_HEIGHT = border.min_height
DETAILS_MAX_WIDTH = border.width / 4
DETAILS_MAX_HEIGHT = border.max_height
c.rect(0, 0, border.width / 4, border.height, fill=True, stroke=False)
c.setFillColor(black)
CONTACT_DETAILS = {"Name": "John Doe", "Email": "john.doe@gmail.com"}
frame = Frame(
    0,
    DETAILS_MAX_HEIGHT,
    DETAILS_MAX_WIDTH,
    DETAILS_MIN_HEIGHT,
    showBoundary=1,
)


frame.addFromList(
    [
        Paragraph(f"{key}: {value}", getSampleStyleSheet()["Normal"])
        for key, value in CONTACT_DETAILS.items()
    ],
    c,
)
c.showPage()
c.save()
