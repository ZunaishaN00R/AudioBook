# Audio Page
# import pyttsx3
# import PyPDF2
# book_path = 'D:/AudioBook Project/Meditations.pdf'
# book = open(book_path, 'rb')
# pdfReader = PyPDF2.PdfReader(book)
# pages = len(pdfReader.pages)
# speaker = pyttsx3.init()
# page = pdfReader.pages[58]
# text = page.extract_text()
# speaker.setProperty('rate',170)
# speaker.say(text)
# speaker.runAndWait()


# # wrong
# import pyttsx3
# import time
# import PyPDF2
# book_path = 'D:/AudioBook Project/Meditations.pdf'
# book = open(book_path, 'rb')
# pdfReader = PyPDF2.PdfReader(book)
# pages = len(pdfReader.pages)
# speaker = pyttsx3.init()
# text = ""
# for page_number in range(len(pdfReader.pages)-150):
#     page = pdfReader.pages[page_number]
#     text += page.extract_text()
#     time.sleep(2)
# speaker.setProperty('rate',170)
# speaker.say(text)
# speaker.runAndWait()
# book.close()


# import pyttsx3
# import time
# import PyPDF2
#
# book_path = 'D:/AudioBook Project/Meditations.pdf'
#
# with open(book_path, 'rb') as book:
#     pdfReader = PyPDF2.PdfReader(book)
#     pages = len(pdfReader.pages)
#     speaker = pyttsx3.init()
#     text = ""
#
#     for page_number in range(len(pdfReader.pages) - 150):
#         page = pdfReader.pages[page_number]
#         text += page.extract_text()
#         time.sleep(2)
#
#     speaker.setProperty('rate', 170)
#     speaker.say(text)
#     speaker.runAndWait()


# import pyttsx3
# import time
# import PyPDF2
#
# book_path = 'D:/AudioBook Project/Meditations.pdf'
# output_audio_path = 'D:/AudioBook Project/Meditations_Audio.mp3'
#
# with open(book_path, 'rb') as book:
#     pdfReader = PyPDF2.PdfReader(book)
#     pages = len(pdfReader.pages)
#     speaker = pyttsx3.init()
#     text = ""
#
#     for page_number in range(len(pdfReader.pages) - 150):
#         page = pdfReader.pages[page_number]
#         text += page.extract_text()
#         time.sleep(2)
#
#     speaker.setProperty('rate', 170)
#     speaker.save_to_file(text, output_audio_path)
#     speaker.runAndWait()




import pyttsx3
import time
import PyPDF2
import sys

book_path = 'D:/AudioBook Project/Meditations.pdf'
output_audio_path = 'D:/AudioBook Project/Meditations_Audio.mp3'

with open(book_path, 'rb') as book:
    pdfReader = PyPDF2.PdfReader(book)
    pages = len(pdfReader.pages)
    speaker = pyttsx3.init()
    text = ""

    for page_number in range(len(pdfReader.pages) - 150):
        page = pdfReader.pages[page_number]
        text += page.extract_text()
        time.sleep(2)

    speaker.setProperty('rate', 170)
    speaker.save_to_file(text, output_audio_path)
    speaker.runAndWait()

# Stop the script after saving the audio file
sys.exit()
