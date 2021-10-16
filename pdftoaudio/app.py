import PyPDF2
import pyttsx3

filepath = input("Enter file name: ")
path = open(filepath + '.pdf.', 'rb')
pdfReader = PyPDF2.PdfFileReader(path)

from_page = pdfReader.getPage(2)

text = from_page.extractText()

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
