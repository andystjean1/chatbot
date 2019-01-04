from PyPDF2 import PdfFileReader as pdf_reader

file = open("groundhogday.pdf", 'rb')

pdf = pdf_reader(file)

print(pdf.isEncrypted)

for i in range(pdf.getNumPages()):
    print("Page ", i, " --------------------------------------")
    print(pdf.getPage(i).extractText())
