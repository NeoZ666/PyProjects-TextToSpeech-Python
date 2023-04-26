# Import the required module for text
# to speech conversion
from PyPDF2 import PdfReader
import pyttsx3

# This module is imported so that we can
# play the converted audio

# The text that you want to convert to audio
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
# Language in which you want to convert
language = 'en'

# TTS = pyttsx3.init("sapi5")
# voices = TTS.getProperty("voices")[0]
# TTS.setProperty('voice',voices)
# TTS.save_to_file(mytext,pdf_name + '.mp3')
# TTS.runAndWait()

def on_end(name, completed):
    global TTS_finished
    TTS_finished = True

def text_to_speech(mytext, pdf_name):
    global TTS_finished
    TTS_finished = False

    TTS = pyttsx3.init("sapi5")
    voices = TTS.getProperty("voices")[0]
    TTS.setProperty('voice',voices)

    TTS.connect('finished-utterance', on_end)
    # TTS.say(mytext)
    TTS.runAndWait()

    while not TTS_finished:
        pass

    TTS.save_to_file(mytext, pdf_name + '.mp3')
    TTS.stop()
    TTS.shutdown()

text_to_speech(mytext, pdf_name)

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
# myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named

# myobj.save(f"TextToSpeech/saved/{pdf_name}.mp3")

# Playing the converted file

# os.system(f"TextToSpeech/saved/{pdf_name}.mp3")