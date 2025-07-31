import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import torch
from transformers import AutoProcessor, AutoModelForVision2Seq
import pyttsx3
import speech_recognition as sr
from googletrans import Translator

# Load model
model_id = "./paligemma-3b-mix-224"  # local model path
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForVision2Seq.from_pretrained(
    model_id,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
).eval()

# TTS engine
engine = pyttsx3.init()

# Translator
translator = Translator()

# GUI
window = tk.Tk()
window.title("Vision Assistant")

img_label = tk.Label(window)
img_label.pack()

img_path = None

def speak(text):
    engine.say(text)
    engine.runAndWait()

def upload_image():
    global img_path
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    img_path = file_path
    img = Image.open(file_path)
    img.thumbnail((300, 300))
    img_tk = ImageTk.PhotoImage(img)
    img_label.config(image=img_tk)
    img_label.image = img_tk

def describe_image():
    if not img_path:
        return
    image = Image.open(img_path).convert("RGB")
    inputs = processor(images=image, text="Description.", return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=50)
    desc = processor.batch_decode(outputs, skip_special_tokens=True)[0]
    text_display.config(text=desc)
    speak(desc)

def ask_question(question):
    if not img_path:
        return
    image = Image.open(img_path).convert("RGB")
    inputs = processor(images=image, text=question, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=50)
    answer = processor.batch_decode(outputs, skip_special_tokens=True)[0]
    text_display.config(text=answer)
    speak(answer)

def ask_from_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        text_display.config(text="🎤 Listening for question...")
        window.update()
        try:
            audio = recognizer.listen(source, timeout=5)
            question = recognizer.recognize_google(audio)
            text_display.config(text=f"❓ Question: {question}")
            ask_question(question)
        except Exception as e:
            text_display.config(text="⚠️ Could not recognize speech.")
            print("Speech Error:", e)

def translate_to_hindi():
    original = text_display.cget("text")
    if original:
        translated = translator.translate(original, dest='hi').text
        text_display.config(text=f"🈂️ Hindi: {translated}")
        speak(translated)

# Buttons
tk.Button(window, text="Upload Image", command=upload_image).pack()
tk.Button(window, text="Describe Image", command=describe_image).pack()
tk.Button(window, text="Ask Question by Voice", command=ask_from_audio).pack()
tk.Button(window, text="Translate Answer to Hindi", command=translate_to_hindi).pack()
text_display = tk.Label(window, text="", wraplength=400, font=("Arial", 12))
text_display.pack()
tk.Button(window, text="Quit", command=window.destroy).pack()

window.mainloop()
