# ✍️ Handwritten Digit Recognition using ANN

## 📌 Project Overview

This project is an end-to-end Deep Learning application that recognizes handwritten digits using an Artificial Neural Network (ANN) built with TensorFlow/Keras.

The model is trained on the famous MNIST dataset containing 70,000 grayscale images of handwritten digits (0–9). Users can upload digit images through a Streamlit web interface, and the trained ANN predicts the digit along with a confidence score.

---

# 🚀 Features

✅ Handwritten digit image upload  
✅ ANN-based digit prediction  
✅ Confidence score display  
✅ Probability distribution chart  
✅ Streamlit interactive UI  
✅ TensorFlow/Keras Deep Learning pipeline  
✅ Real-time inference system  

---

# 🧠 Model Architecture

The Artificial Neural Network was built using TensorFlow/Keras Sequential API.

## Architecture

```python
Dense(128, activation='relu')
Dropout(0.2)

Dense(64, activation='relu')
Dropout(0.2)

Dense(10, activation='softmax')
```

## Key Components

- **ReLU Activation** → Enables non-linear learning
- **Dropout Layers** → Prevent overfitting
- **Softmax Output Layer** → Produces probability distribution for digits 0–9

---

# 📊 Model Performance

## ✅ Final Test Accuracy

```text
97.75%
```

The ANN generalizes effectively on unseen handwritten digit images from the MNIST test dataset.

---

# 🛠️ Tech Stack

| Area | Technology |
|------|-------------|
| Language | Python |
| Deep Learning | TensorFlow / Keras |
| Frontend | Streamlit |
| Visualization | Matplotlib |
| Numerical Computing | NumPy |
| Image Processing | PIL (Pillow) |

---

# 📂 Project Structure

```text
MNIST_ANN_Project/
│
├── models/
│   └── mnist_ann_model.keras
│
├── notebooks/
│   └── training.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🔄 Project Workflow

```text
Image Upload
      ↓
Image Preprocessing
      ↓
Normalization
      ↓
Flattening (28×28 → 784)
      ↓
ANN Prediction
      ↓
Digit Output + Confidence Score
```

---

# ▶️ Run Locally

## 1️⃣ Clone Repository

```bash
git clone <your-repository-link>
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd MNIST_ANN_Project
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

# 🌐 Deployment

This project can be deployed easily using:

- Streamlit Cloud
- GitHub

---

# 📚 Concepts Learned

Through this project, the following concepts were implemented and understood:

- Artificial Neural Networks (ANN)
- TensorFlow/Keras Workflow
- Image Preprocessing
- Normalization
- Dropout Regularization
- Softmax Classification
- Streamlit Web Applications
- Model Deployment
- Deep Learning Inference Pipelines

---

# 🎯 Future Improvements

✅ Drawing canvas for live digit input  
✅ CNN-based architecture upgrade  
✅ Better preprocessing for real-world handwritten images  
✅ Top-3 prediction display  
✅ Dark mode UI improvements  

---

# 👨‍💻 Author

Developed as an end-to-end Deep Learning project using TensorFlow, ANN, and Streamlit.