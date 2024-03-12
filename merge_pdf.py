from pypdf import *
import os

merge = PdfWriter()
files = os.listdir()
new = []
for file in files:
    if file.endswith(".pdf"):
        new.append(file)

for i in new:
    merge.append(i)
    new.sort()

merge.write("merge1.pdf")
merge.close()