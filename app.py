from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

model = tf.keras.models.load_model("crop_model.h5")

def predict_image(img):
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    return np.argmax(prediction)

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    img = Image.open(file)
    result = predict_image(img)

    diseases = ["Healthy", "Leaf Spot", "Rust", "Blight"]

    return jsonify({
        "disease": diseases[result]
    })

if __name__ == "__main__":
    app.run(debug=True)
