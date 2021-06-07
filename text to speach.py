from gtts import gTTS
import os 

fh = open("test.txt", "r")
myText = fh.read().replace("\n","")

langue = 'en'

output = gTTS(text=myText, lang=langue, slow=False)

output.save("output.mp3")
fh.close() 
os.system("start output.mp3")