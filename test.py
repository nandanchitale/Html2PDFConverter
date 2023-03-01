from weasyprint import HTML

# Load the HTML file
html = HTML(filename='test.html')

# Set the PDF options
pdf_options = {
    'page-size': 'A4',
    'margin-top': '1cm',
    'margin-right': '1cm',
    'margin-bottom': '1cm',
    'margin-left': '1cm'
}

# Generate the PDF
html.write_pdf('records.pdf', stylesheets=['css/style.css'])