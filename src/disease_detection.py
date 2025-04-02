import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load pre-trained model
model = load_model("models/trained_model.h5")

def predict_disease(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))  # Resize for model input
    image = np.array(image) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension

    prediction = model.predict(image)
    class_index = np.argmax(prediction)
    
    # Sample disease classes
    classes = ["Healthy", "Bacterial Spot", "Leaf Mold", "Yellow Leaf Curl Virus"]
    detected_disease = classes[class_index]

    print(f"Disease detected: {detected_disease}")
    return detected_disease

if __name__ == "__main__":
    predict_disease("datasets/sample_images/crop_image.jpg")
