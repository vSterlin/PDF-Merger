import os
import sys
from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader


files = os.listdir()

pdfs = list(filter(lambda f: f.endswith(".pdf"), files))

if len(pdfs) == 0:
  raise Exception("No pdf files in this directory")

m = PdfFileMerger()

for pdf in pdfs:
  m.append(pdf)

try:
  name = sys.argv[1]
  if not name.endswith(".pdf"):
    name += ".pdf"
except:
  name = "merged.pdf"

m.write(name)

m.close()