import cv2
import numpy as np

def analyze_soil(image_path):
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define brown color range for soil detection
    lower_brown = np.array([10, 50, 50])
    upper_brown = np.array([30, 255, 255])

    mask = cv2.inRange(hsv, lower_brown, upper_brown)
    soil_percentage = (np.sum(mask) / mask.size) * 100

    print(f"Soil Quality Percentage: {soil_percentage:.2f}%")
    return soil_percentage

if __name__ == "__main__":
    analyze_soil("datasets/sample_images/soil.jpg")
