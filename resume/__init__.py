from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

c = canvas.Canvas("hello.pdf")
width, height = A4

c.drawString(0, height, "Hello, World!")
c.showPage()
c.save()
