# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 13:40:58 2019

@author: Satyam
"""

from PIL import Image
import pytesseract
from googletrans import Translator  # Import Translator module from googletrans package

im = Image.open("CV.jpg")

text = pytesseract.image_to_string(im, lang = 'eng')

print(text) 

translator = Translator() # Create object of Translator.
ab = translator.translate(text, dest = 'hi')
print(ab)
