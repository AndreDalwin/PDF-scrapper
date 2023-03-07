import PyPDF2

pdf_file = open("powerpoint.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(pdf_file)

text = ""

for i in range(len(pdf_reader.pages)):
    text += pdf_reader.pages[i].extract_text()

with open("output.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write(text)

pdf_file.close()