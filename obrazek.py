import os
from PIL import Image
print(os.getcwd())
directory_img = "/home/student" + "/images/"
if os.path.exists("/home/student/opt/icons"):
  print("sciezka istnieje")  
else:
  os.makedirs("/home/student/opt/icons")

old_files = []
new_files = []
names_list = []
for file in os.listdir(directory_img):
  os.chdir(directory_img)
  names = os.path.splitext(file)
  names_list.append(names[0])
  #print(names)
  #print(type(names))
  im = Image.open(file)
  im.rotate(-90)
  ims = im.resize((128, 128))
  old_files.append(ims)


for file in old_files:
  if file.mode != "RGB":
    imm = file.convert("RGB")
    new_files.append(imm)
  else:
    new_files.append(file)
#print(names_list)
os.chdir("/home/student/opt/icons")
for file in new_files:
  for nazwa in names_list:
    ims = file.save(nazwa, "JPEG")
