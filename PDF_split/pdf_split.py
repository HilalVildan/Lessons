from PyPDF4 import PdfFileReader, PdfFileWriter

input_pdf = PdfFileReader ("./Desktop/Lessons/PDF_split/Tiny_Python_Projects.pdf")

pages = [3,6,9]
output = PdfFileWriter()
for page_num in pages:
    output.addPage(input_pdf.getPage(page_num))

with open("./Desktop/Lessons/PDF_split/Tiny_Python02.pdf", "wb") as output_stream:
    output.write(output_stream)
    output_stream.close()
    print(f"yeni pdf dosyasi {output_stream.name} olusturuldu")

