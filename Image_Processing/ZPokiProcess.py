from pathlib import Path
from PIL import Image, ImageFilter
from os import chdir
import glob

safe = Path.cwd()


def imge_pross(folder_dir, image_dir):
    chdir(f'{folder_dir}')
    img = Image.open(f'{image_dir}')
    filimg = img.filter(ImageFilter.BLUR)
    filimg.save("Blur", "PNG")
    filimg = img.filter(ImageFilter.SMOOTH)
    filimg.save("Smooth", "PNG")
    filimg = img.convert('L')
    filimg.save("Mono", "PNG")
    filimg = img.resize((300, 300))
    filimg.save("Resized", "PNG")
    filimg = img.crop((100, 100, 400, 400))
    filimg.save("Cropped", "PNG")
    img.thumbnail((400, 200))
    img.save('RResized.jpg')
    chdir(f'{safe}')


all_dir = glob.glob('/home/ijek/Documents/Python_Prac/Projects/Image_Processing/*jpg')
image_stem = []
image_name = []
for a in all_dir:
    f = Path(a)
    image_stem.append(f.stem)
    image_name.append(f.name)
c = 0
for i in image_stem:
    b = Path(f'Documents/Python_Prac/Projects/Image_Processing/{i}').resolve()
    b.mkdir(parents=True, exist_ok=True)
    new_path = Path(
        f'/home/ijek/Documents/Python_Prac/Projects/Image_Processing/{i}/{image_name[c]}')
    Path(f'{all_dir[c]}').replace(f'{new_path}')
    imge_pross(b, new_path)
    c = c+1
