from os import chdir
from pathlib import Path
import img2pdf
# import PyPDF2

# def all_process(path):
    # png=glob(path+'*PNG')
    # for i in png:
    #     a=Path(i)
    #     name=a.stem
    #     im1=Image.open(i)
    #     im1.save(path+name+'.jpg')


def all_process(path):
    path = Path(path)
    images=path.rglob('*jpg')
    name=[]
    for i in images:
        f=Path(i)
        name.append(f.name)
    chdir(path)
    file=open("Output.pdf","wb")
    file.write(img2pdf.convert(name))
    file.close()

path=input('Image Foleder Director : ')

all_process(path)