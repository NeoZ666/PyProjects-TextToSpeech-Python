from gtts import gTTS
from PyPDF2 import PdfReader
from pathlib import Path

# path = Path('TextToSpeech/pdfs/Freedom_from_Porn.pdf')
def pdfToMusic():
    if path.exists():
        reader = PdfReader(pathFunction)
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
        # print(mytext)
        def text_to_speech(mytext, pdf_name):
            tts = gTTS(text=mytext, lang='en')
            tts.save(pdf_name + '.mp3')
            
        text_to_speech(mytext, pdf_name)
    else:
        print('File does not exist.')

def pathFunction(file_path: str) -> Path:
    path = Path(file_path)
    return path

# def provideStart(start):
#     i = start


pathFunction('TextToSpeech/pdfs/Freedom_from_Porn.pdf')
pdfToMusic()