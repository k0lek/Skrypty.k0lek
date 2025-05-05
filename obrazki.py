import glob, os
from PIL import Image


"""size = 640, 640

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
        im.thumbnail(size)
        im.save(file + ".thumbnail", "JPEG")"""
#path = "~/scripts/supplier-data/images"
"""obrazki = os.listdir("obrazki")
size = (640, 640)
for obrazek in obrazki:
  im = Image.open("obrazki/" + obrazek)
  im.convert("RGB")
  im2 = im.resize((640,640))
  im2.save("obrazki2/" + obrazek + ".jpg", "JPEG")
  print(im2.size, im2.mode)"""
"""  with Image.open("obrazki/" + obrazek) as file:
    file.convert("RGB")
    file.resize(size)
    file.save("obrazki2/" + obrazek + ".jpg", "JPEG")
    print(file.size, file.mode)"""
    #!/usr/bin/env python3
path = os.getcwd() + "/supplier-data/images/"
obrazki = os.listdir(path)
size = (640, 640)
for obrazek in obrazki:
#  print(obrazek)
  if obrazek.endswith(".tiff"):
    print(obrazek)
    im = Image.open(path + obrazek)
    im2 = im.convert("RGB")
    im3 = im2.resize((640,640))
    im3.save(path + obrazek.strip(".tiff") + ".jpeg", "JPEG")
    print(im3.size, im3.mode)
