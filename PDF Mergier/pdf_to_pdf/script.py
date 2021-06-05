from pathlib import Path
from PyPDF2 import PdfFileMerger

def pdfm(path):
    path=Path(path)
    lis=path.rglob('*pdf')
    merger = PdfFileMerger()
    name=[]
    for i in lis:
        name.append(str(i))

    for item in name:
        merger.append(item)
    merger.write(str(path)+'/Output.pdf')
    merger.close()

path = input('PDF Folder Directory : ')
pdfm(path)