import speech_recognition as sr
import sys
import subprocess

video = sys.argv[1]

file = "audio.wav"
print("Extracting audio....")
subprocess.call(f'ffmpeg -i {video} -ab 160k -ac 2 -ar 44100 {file}', shell = True)
print("Done")
recognizer = sr.Recognizer()
texts = ""
with sr.AudioFile(file) as source:
    data = recognizer.record(source)
    print("Recognizing text....")
    texts = recognizer.recognize_sphinx(data)
print("Done")
text = open("sub.txt", "w")
text.write(texts)
text.close()