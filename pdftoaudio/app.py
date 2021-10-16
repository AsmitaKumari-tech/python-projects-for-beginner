import PyPDF2
import pyttsx3

task = input("What you want to do? Read a (text or pdf)")

if(task == 'pdf' or task == 'PDF'):
    filepath = input("Enter file name: ")
    path = open(filepath + '.pdf.', 'rb')
    pdfReader = PyPDF2.PdfFileReader(path)
    from_page = pdfReader.getPage(1)
    text = from_page.extractText()
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()
else:
    text = input("Enter the text: ")
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()
