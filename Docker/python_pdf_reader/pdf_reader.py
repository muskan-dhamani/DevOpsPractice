import PyPDF2

def read_pdf(file_path):
    # Open the PDF file
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # Get the number of pages
        num_pages = len(reader.pages)

        # Loop through all pages and extract text
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text()
            print(f"Page {page_num + 1} Text:\n{text}\n")

# Example usage
if __name__ == "__main__":
    pdf_path = 'testpdf.pdf'  # Change this to the correct path to your PDF
    read_pdf(pdf_path)

