from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(filename):
    # Create a canvas object
    c = canvas.Canvas(filename, pagesize=letter)
    
    # Add some text to the PDF
    c.drawString(100, 750, "Hello, this is a PDF created using ReportLab.")
    
    # Save the PDF to the file
    c.save()

# Example usage: Create a PDF file named 'output.pdf'
create_pdf("testpdf.pdf")

