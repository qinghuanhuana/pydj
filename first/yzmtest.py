# coidng=utf-8
# a = 1366271110
# n = 0
# for n in  range(90):
#     a+=1
#     b=str(a)
#     with open('F:/pydj/first/mobile.txt','a') as fd:
#         fd.write(b+"\n")

# import time
# a = time.time()
# print (a)
# print(int(a))
# print(int(round(a*1000)))

import pytesseract
from PIL import Image
# pytesseract.pytesseract.tesseract_cmd = r'd:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
img = Image.open(r'.\photo\22.png')
img= img.convert('RGBA')
pixdata = img.load()
for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pixdata[x,y][0] <90:
            pixdata[x,y] = (0,0,0,255)
for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pixdata[x, y][1] < 136:
            pixdata[x, y] = (0, 0, 0, 255)
for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pixdata[x, y][2] > 0:
            pixdata[x, y] = (255, 255, 255, 255)
vcode = pytesseract.image_to_string(img)
print(vcode)

