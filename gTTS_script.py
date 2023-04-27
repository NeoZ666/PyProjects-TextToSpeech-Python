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

def pathFunction(file_path: str):
    path = Path(file_path)
    reader = PdfReader(pathFunction)
    global length
    length = len(reader.pages)
    return path

def provideStartAndEnd(start: int = None, end: int = length) -> tuple[int, int]:
    if start is None or start < 0:
        start = 1
    else:
        start += 1
    
    if end > start:
        if end is None or end < 0:
            end = length + 1
        else:
            end += 1
        return (start, end)
    else:
        print("The Page End must be greater than the Page Start")




pathFunction('TextToSpeech/pdfs/Freedom_from_Porn.pdf')
provideStartAndEnd()
pdfToMusic()