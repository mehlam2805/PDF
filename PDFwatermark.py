import PyPDF2
import sys

pdf_file = sys.argv[1]

my_file = open(f'C:\\Users\\ezzi9\\Desktop\\{pdf_file}', 'rb')
watermark = open('C:\\Users\\ezzi9\\Desktop\\wtr.pdf', 'rb')

reader1 = PyPDF2.PdfFileReader(my_file)
wtr_reader = PyPDF2.PdfFileReader(watermark)
writer = PyPDF2.PdfFileWriter()

waterpage = wtr_reader.getPage(0)

for pages in range(reader1.numPages):
    reader1.getPage(pages).mergePage(waterpage)
    writer.addPage(reader1.getPage(pages))

new = open('water.pdf', 'wb')
writer.write(new)
