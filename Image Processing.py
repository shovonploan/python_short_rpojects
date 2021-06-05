from PIL import Image, ImageFilter

img = Image.open('/home/ijek/Documents/Python_Prac/Projects/P/bulbasaur.jpg')
img.show()
print(img)
print(img.format)
print(img.size)
print(img.mode)
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
