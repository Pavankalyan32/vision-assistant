import cv2
import pytesseract
import pyttsx3
from PIL import Image
from transformers import AutoProcessor, AutoModelForVision2Seq
from transformers import pipeline
import torch

# Optional: Set this only if tesseract is not in PATH
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load image
image_path = "test.jpg"  # change to your image file
image_bgr = cv2.imread(image_path)
if image_bgr is None:
    raise ValueError(f"Could not read image at {image_path}")
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
pil_image = Image.fromarray(image_rgb)

# Step 1: Extract text using OCR
ocr_text = pytesseract.image_to_string(pil_image)
print("🔍 OCR Output:\n", ocr_text)

# Step 2: Image captioning using Gemma (replace with your path if local)
print("🧠 Generating caption...")
model_id = "google/paligemma-3b-mix-224"  # or your local path if downloaded
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForVision2Seq.from_pretrained(model_id, torch_dtype=torch.float32)

inputs = processor(images=pil_image, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=50)
caption = processor.batch_decode(outputs, skip_special_tokens=True)[0]
print("🖼️ Caption:", caption)

# Step 3: Combine text sources
full_context = caption.strip() + "\n" + ocr_text.strip()

# Step 4: Ask a question (hardcoded for now, can add GUI later)
question = "What is written in the image?"  # or dynamically input by user

# Use a lightweight QA model (Gemma isn't for text QA yet)
print("❓ Answering question...")
qa_pipe = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
result = qa_pipe(question=question, context=full_context)
answer = result['answer']
print("✅ Answer:", answer)

# Step 5: Speak out the result
engine = pyttsx3.init()
engine.say("The answer is: " + answer)
engine.runAndWait()
