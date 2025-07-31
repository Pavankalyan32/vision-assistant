from transformers import AutoModelForVision2Seq, AutoProcessor

model_id = "google/paligemma-3b-mix-224"
save_dir = "paligemma-3b-mix-224"

# Download & save processor + model locally
print("Downloading model, please wait...")
processor = AutoProcessor.from_pretrained(model_id)
processor.save_pretrained(save_dir)

model = AutoModelForVision2Seq.from_pretrained(model_id)
model.save_pretrained(save_dir)

print("✅ Model saved locally to:", save_dir)