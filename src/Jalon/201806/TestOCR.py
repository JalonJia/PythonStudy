'''
Created on 2018年6月17日

@author: jalon
'''

import pytesseract
from PIL import Image

# open image
image = Image.open('c:\\x.jpg')
code = pytesseract.image_to_string(image, lang='chi_sim')
print(code)