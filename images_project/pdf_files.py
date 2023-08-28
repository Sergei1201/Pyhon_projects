import PyPDF2

# Read a file
with open('sample.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]
    page_readable = page.extract_text()
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open('written.pdf', 'wb') as new_file:
        writer.write(new_file)
