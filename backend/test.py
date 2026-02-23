import numpy as np
from PIL import Image
from tensorflow import keras

# Load model
model = keras.models.load_model("cattle_model_v2.keras")

class_names = [
    "brahman",
    "brahman_cross",
    "cholistani",
    "cholistani_cross",
    "dhani",
    "fresian",
    "fresian_cross",
    "kankarej",
    "sahiwal",
    "sahiwal_cross",
    "sibbi",
    "unidentified"
]

def predict_image(image_path):
    # Load and preprocess image
    image = Image.open(image_path).convert("RGB")
    image = image.resize((160, 160))  # Must match training size
    
    img_array = np.array(image)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Make prediction
    prediction = model.predict(img_array)

    # Get results
    confidence = float(np.max(prediction[0]))
    predicted_class = class_names[np.argmax(prediction[0])]

    print("\nPrediction array:", prediction)
    print("Confidence:", confidence)
    print("Predicted class:", predicted_class)

# Change image name here
predict_image("brahman_1.jpg")