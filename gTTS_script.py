from gtts import gTTS
from PyPDF2 import PdfReader
import os

path = 'TextToSpeech/pdfs/BOOKNAME.pdf'
reader = PdfReader(path)
path = path.split("/")
pdf_name = path[2].split(".")[0]

i=7
textfile = []
while i<int(len(reader.pages)):
    page = reader.pages[i]
    text = page.extract_text()
    textfile.append(text)
    i = i+1

mytext = ''.join(textfile)
print(mytext)
# def text_to_speech(mytext, pdf_name):
#     tts = gTTS(text=mytext, lang='en')
#     tts.save(pdf_name + '.mp3')
    
# text_to_speech(mytext, pdf_name)