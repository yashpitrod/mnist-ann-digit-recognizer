import streamlit as st
import numpy as np
from PIL import Image
import onnxruntime as ort
import pandas as pd

st.set_page_config(
    page_title="MNIST Digit Recognizer",
    page_icon="✍️",
    layout="centered"
)

st.title("✍️ Handwritten Digit Recognition")

st.write("Upload a handwritten digit image and let the ANN predict it.")

st.sidebar.header("About")

st.sidebar.write("""
This project uses:

- TensorFlow/Keras
- Artificial Neural Networks
- MNIST Dataset
- Streamlit
""")

# IMAGE INPUT
uploaded_file = st.file_uploader(
    "Upload Digit Image",
    type=['png', 'jpg', 'jpeg']
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", width=200)

# Load model once at startup
@st.cache_resource
def load_trained_model():
    return ort.InferenceSession("models/mnist_ann_model.onnx")

model = load_trained_model()

def predict_digit(image):

    image = image.convert('L')

    image = image.resize((28, 28))

    image_array = np.array(image)

    # Invert colors
    image_array = 255 - image_array

    # Normalize
    image_array = image_array / 255.0

    # Flatten
    image_array = image_array.reshape(1, 784)

    prediction = model.run(None, {"dense_input": image_array.astype("float32")})[0]

    predicted_digit = np.argmax(prediction)

    confidence = np.max(prediction)

    return predicted_digit, confidence, prediction[0]

if uploaded_file is not None:

    digit, confidence, probabilities = predict_digit(image)

    # Large Prediction Display
    st.subheader("Prediction")

    st.metric(
        label="Predicted Digit",
        value=digit
    )

    st.metric(
        label="Confidence",
        value=f"{confidence * 100:.2f}%"
    )

    prob_df = pd.DataFrame({
        'Digit': list(range(10)),
        'Probability': probabilities
    })

    st.subheader("Prediction Probabilities")

    st.bar_chart(
        prob_df.set_index('Digit')
    )