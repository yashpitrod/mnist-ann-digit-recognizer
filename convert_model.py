"""
Verify that the Keras model loads correctly
Run this script locally to test
"""
import tensorflow as tf
import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

print("📥 Loading Keras model...")
try:
    model = tf.keras.models.load_model('models/mnist_ann_model.keras')
    print(f"✅ Model loaded successfully!")
    print(f"📊 Model summary:")
    model.summary()
    print(f"✅ Model is ready for deployment!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
