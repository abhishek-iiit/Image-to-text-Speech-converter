#importing the Libraries
from gtts import gTTS           # used for converting text to speech
import PIL                      # Python Imaging Library
import gtts                     # Google's text to Speech API
import pytesseract              # used for image to text conversion using OCR
from tkinter import filedialog  # Used to provide GUI open/save feature
from tkinter import *
from PIL import Image,ImageTk   # used for handling image type file
import pyperclip

#defining the Window
window = Tk()
window.geometry('1280x832')
window.resizable(0, 0)
window.title("Image-Text-Speech Converter @abhishek-iiit")
image=Image.open("_bg_.jpg")
photo=ImageTk.PhotoImage(image)
lab=Label(image=photo,bg='#8fb5c2')
lab.pack()

#Defining the Labels
message = Label(window, text="Image-Text-Speech Converter @abhishek-iiit" ,bg="#000000"  ,fg="#FFFF00"  ,width=50  ,height=3,font=('Helvetica', 35, 'italic bold '))
message.place(x=60, y=10)
message = Label(window, text="Note : Text field in only for 'Text-to-Audio' file\n RIGHT CLICK to paste the text copied from 'Pic-to-Text' file" ,bg="#000000"  ,fg="#FF0000"  ,width=70  ,height=2,font=('Helvetica', 15, 'italic bold '))
message.place(x=130, y=120)
message = Label(window, text="" ,bg="grey"  ,fg="black"  ,width=50  ,height=12, activebackground = "yellow" ,font=('Helvetica', 20 , ' bold ')) 
message.place(x=150, y=170)
lbl2 = Label(window, text="Enter text :",width=20  ,fg="white"  ,bg="#000000"    ,height=2 ,font=('Helvetica', 20 , ' bold ')) 
lbl2.place(x=150, y=490)
txt2 = Entry(window,width=40  ,bg="white" ,fg="black",font=('Helvetica', 20 , ' bold '))
txt2.place(x=390, y=505)

#Defining the funtions
def PicTexts():
    window.filename =  filedialog.askopenfilename()
    # provides a dialog box for asking file to open and returns it's path
    img= PIL.Image.open(window.filename)      # opening image type file
    result= pytesseract.image_to_string(img)   # converting image to text
    res = "***Text copied***\n" + result
    pyperclip.copy(res)
    message.configure(text= res)
    if(result==""):
        res = "Sorry!! Nothing recogonized"
        message.configure(text= res)

def picSpeechs():
    window.filename =  filedialog.askopenfilename()
    # provides a dialog box for asking file to open and returns it's path
    img= PIL.Image.open(window.filename)      # opening image type file
    result= pytesseract.image_to_string(img)   # converting image to text
    if(result==""):
        res = "Sorry!! Nothing recogonized"
        message.configure(text= res)   
    res= gTTS(result)                # converting text to speech  .... Internet required
    window.filename =  filedialog.asksaveasfilename()
    # provides a dialog box for asking file to save and returns it's path
    res.save(window.filename+ '.mp3')     # inbuit audio saving function
    res = "Saved"
    message.configure(text= res)  

def TextSpeechs(): 
    textInp= (txt2.get())
    res= gTTS(textInp)
    window.filename =  filedialog.asksaveasfilename()
    res.save(window.filename+ '.mp3')
    res = "Saved"
    message.configure(text= res)

#Defining the buttons
pictext = Button(window, text="Pic-to-Text", command=PicTexts  ,fg="red"  ,bg="white"  ,width=20  ,height=3, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
pictext.place(x=1000, y=170)
picspeech = Button(window, text="Pic-to-Audio", command=picSpeechs  ,fg="red"  ,bg="white"  ,width=20  ,height=3, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
picspeech.place(x=1000, y=270)
textspeech = Button(window, text="Text-to-Audio", command=TextSpeechs  ,fg="red"  ,bg="white"  ,width=20  ,height=3, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
textspeech.place(x=1000, y=370)
quitWindow = Button(window, text="Quit", command=window.destroy  ,fg="red"  ,bg="white"  ,width=17  ,height=2, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
quitWindow.place(x=1060, y=760)

window.mainloop()
