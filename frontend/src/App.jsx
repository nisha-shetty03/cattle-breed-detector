import { useState } from "react";

function App() {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    setImage(file);
    setPreview(URL.createObjectURL(file));
    setResult(null);
  };

  const handleUpload = async () => {
    if (!image) return alert("Please select an image");

    const formData = new FormData();
    formData.append("file", image);

    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) throw new Error("Failed to fetch from backend");

      const data = await response.json();
      setResult(data);
    } catch (error) {
      alert("Error connecting to backend: " + error.message);
    }

    setLoading(false);
  };

  return (
    <div style={{ textAlign: "center", padding: "40px", fontFamily: "Arial" }}>
      <h1 style={{ fontSize: "32px", marginBottom: "20px" }}>🐄 Cattle Breed Classification</h1>

      <input type="file" onChange={handleImageChange} />

      {preview && (
        <img src={preview} alt="preview" style={{ width: "300px", marginTop: "20px" }} />
      )}

      <button
        onClick={handleUpload}
        style={{ marginTop: "20px", padding: "10px 20px", fontSize: "16px" }}
      >
        {loading ? "Predicting..." : "Classify"}
      </button>

      {result && (
        <div style={{
          marginTop: "30px",
          textAlign: "left",
          display: "inline-block",
          padding: "20px",
          border: "1px solid #ddd",
          borderRadius: "8px"
        }}>
          <h2>Prediction: {result.predicted_class}</h2>
          <p><strong>Confidence:</strong> {result.confidence}%</p>
          <p><strong>Origin:</strong> {result.origin}</p>
          <p><strong>Milk Yield:</strong> {result.milk_yield}</p>
          <p><strong>Type:</strong> {result.type}</p>
          <p><strong>Description:</strong> {result.description}</p>
          <p><strong>Uses:</strong> {result.uses}</p>
        </div>
      )}
    </div>
  );
}

export default App;