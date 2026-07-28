# 🐄 Cattle Breed Detector

An image-based application that identifies the breed of cattle from a photo and provides useful breed-specific information — including origin, typical milk yield, and best use — to help farmers, veterinarians, and researchers make informed decisions.

## 📖 Overview

Cattle Breed Detector uses a computer vision model to classify the breed of cattle from an uploaded image. Beyond simple classification, it enriches the result with practical information about the breed, making it useful for agricultural and dairy-related decision-making.

## ✨ Features

- 📷 **Image-based breed detection** — upload a cattle image and get an instant breed prediction
- 🌍 **Origin information** — learn where the breed originates from
- 🥛 **Milk yield insights** — see typical milk production for the detected breed
- 🐮 **Best use recommendations** — dairy, draught, or dual-purpose guidance
- 🌐 **Simple web interface** — accessible directly from the browser

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Model / CV Pipeline | Python, TensorFlow |
| Backend | FastAPI |
| Frontend | React (Vite), JavaScript, CSS |
| Deployment | Render |

## 🚀 How It Works

1. User uploads an image of a cow/cattle through the web interface.
2. The Python-based model processes the image and predicts the breed.
3. The app looks up breed-specific details (origin, milk yield, best use).
4. Results are displayed to the user through the web front-end.

## ⚙️ Installation & Usage

Clone the repository first:

```bash
git clone https://github.com/Nishashetty03/<repo-name>.git
cd <repo-name>
```

**Backend** (from `backend/`):

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**Frontend** (from `frontend/`):

```bash
npm install
VITE_API_URL=https://YOUR-API.onrender.com npm run dev
```

Once both are running, open the frontend in your browser and upload a cattle image to get started.

## 📁 Project Structure

- `backend/` — FastAPI + TensorFlow model
- `frontend/` — React (Vite) UI

## 📊 Model Details

- **Input:** Cattle image (JPG/PNG)
- **Output:** Predicted breed + origin, milk yield, and best-use information
- *(Add details here: dataset used, number of breed classes, model architecture, accuracy if available)*

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to open an issue or submit a pull request.
