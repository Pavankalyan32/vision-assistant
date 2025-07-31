import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import torch
from transformers import pipeline
import pyttsx3
import pytesseract
import speech_recognition as sr
from googletrans import Translator

# Load Gemma image captioning pipeline
caption_pipeline = pipeline(
    "image-text-to-text",  # ✅ correct
    model="google/paligemma-3b-mix-224",
    model_kwargs={"torch_dtype": torch.float32},
    device="cpu"
)

# Load OCR
def perform_ocr(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)

# Speak text
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Recognize speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, "Listening...\n")
            audio = r.listen(source)
            query = r.recognize_google(audio)
            result_text.insert(tk.END, f"You asked: {query}\n")
            return query
        except Exception as e:
            result_text.insert(tk.END, f"Speech recognition error: {str(e)}\n")
            return ""

# Translate text
translator = Translator()
def translate_text(text, dest_lang="hi"):
    try:
        translation = translator.translate(text, dest=dest_lang)
        return translation.text
    except Exception as e:
        return f"Translation failed: {e}"

# GUI App
def select_image():
    global uploaded_image
    file_path = filedialog.askopenfilename()
    if file_path:
        uploaded_image = file_path
        img = Image.open(file_path)
        img.thumbnail((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk

def describe_image():
    if uploaded_image:
        image = Image.open(uploaded_image)
        prompt = "<image> Description."
        
        # ✅ Correct key is "images"
        result = caption_pipeline({"images": image, "text": prompt}, max_new_tokens=50)
        
        caption = result[0]["generated_text"]
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Caption: {caption}")
        speak_text(caption)

def perform_ocr_gui():
    if uploaded_image:
        text = perform_ocr(uploaded_image)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"\U0001F50D OCR Output:\n{text}\n")
        speak_text(text)

def ask_question():
    query = recognize_speech()
    if query and uploaded_image:
        prompt = f"<image> {query}"
        image = Image.open(uploaded_image)
        result = caption_pipeline({"image": image, "text": prompt}, max_new_tokens=50)
        answer = result[0]["generated_text"]
        result_text.insert(tk.END, f"\u2705 Answer: {answer}\n")
        speak_text(answer)

def translate_caption():
    text = result_text.get("1.0", tk.END)
    translated = translate_text(text, dest_lang="hi")
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, translated)
    speak_text(translated)

# Build GUI
app = tk.Tk()
app.title("Gemma Vision Assistant")
app.geometry("600x600")

upload_btn = tk.Button(app, text="Upload Image", command=select_image)
upload_btn.pack(pady=5)

describe_btn = tk.Button(app, text="Describe Image", command=describe_image)
describe_btn.pack(pady=5)

ocr_btn = tk.Button(app, text="Read Text (OCR)", command=perform_ocr_gui)
ocr_btn.pack(pady=5)

ask_btn = tk.Button(app, text="Ask Question", command=ask_question)
ask_btn.pack(pady=5)

translate_btn = tk.Button(app, text="Translate to Hindi", command=translate_caption)
translate_btn.pack(pady=5)

image_label = tk.Label(app)
image_label.pack(pady=10)

result_text = tk.Text(app, height=15, width=70)
result_text.pack(pady=10)

app.mainloop()
