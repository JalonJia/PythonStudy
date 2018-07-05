'''
Created on 2018年6月17日

@author: jalon
'''

import pytesseract
from PIL import Image

# open image
#image = Image.open('D:\\StudyPic\\Class1\\2.jpg')
#code = pytesseract.image_to_string(image, lang='chi_sim')
#print(code)

image = Image.open('D:\\StudyPic\\Class2\\1.jpg')
code = pytesseract.image_to_string(image, lang='chi_sim')
print(code)
print('=' * 100)