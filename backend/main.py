from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import io
import os

# Import breed details
from utils.breed_info import breed_details

app = FastAPI()

# Enable CORS so frontend can connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://cattle-breed-detector-q9v9v16nn-nisha-shetty03s-projects.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Path to your model
MODEL_PATH = "cattle_model_v3.keras"  # <-- if inside backend/
# MODEL_PATH = "model/cattle_model_v2.keras"  # <-- if inside backend/model/

# Check if model file exists
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}")

# Load model
model = load_model(MODEL_PATH,compile=False)
model.save("cattle_model_v3.keras")
# Class names (must match your model training)
class_names = list(breed_details.keys())
print(class_names)

@app.get("/")
def home():
    return {"message": "Cattle Breed Prediction API Running"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Read image
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        image = image.resize((160, 160))

        # Convert to array
        img_array = np.array(image) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Predict
        prediction = model.predict(img_array)

        predicted_index = int(np.argmax(prediction))
        print("predicted index:",predicted_index)
        print("predicted class",class_names[predicted_index])
        # Safety check
        if predicted_index >= len(class_names):
            return {"error": "Model class index mismatch. Check class_names."}
        predicted_class = class_names[predicted_index]
        confidence = float(np.max(prediction)) * 100
        if confidence<60:
            predicted_class="unrecognized cattle breed"

        # Get breed details
        details = breed_details.get(predicted_class, {})

        # Return in frontend-friendly format
        response = {
            "predicted_class": predicted_class,
            "confidence": round(confidence, 2),
            "origin": details.get("origin", ""),
            "milk_yield": details.get("milk_yield", ""),
            "type": details.get("type", ""),
            "description": details.get("description", ""),
            "uses": details.get("uses", ""),
        }

        return response

    except Exception as e:
        return {"error": str(e)}