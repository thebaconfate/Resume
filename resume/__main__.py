from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import Color
from resume.border import Border


c = Canvas("hello.pdf")
left_border = Color(37, 150, 190)
border = Border(*A4)
print(border.min_width, border.min_height)
print(border.max_width, border.max_height)
print(border.width, border.height)

c.drawString(border.min_width, border.min_height, "Hello, World!")
c.rect(0, 0, border.min_width * 2, border.height, fill=left_border)
c.showPage()
c.save()
