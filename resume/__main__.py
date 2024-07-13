from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import Color, blue
from resume.border import Border


c = Canvas("hello.pdf")
left_border = Color(37 / 255, 150 / 255, 190 / 255)
border = Border(*A4)
print(border.min_width, border.min_height)
print(border.max_width, border.max_height)
print(border.width, border.height)

c.drawString(border.min_width, border.min_height, "Hello, World!")
c.setFillColor(left_border)
c.rect(0, 0, border.min_width * 2, border.height, fill=True, stroke=False)
c.showPage()
c.save()
