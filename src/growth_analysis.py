import cv2
import numpy as np

def compare_images(image1_path, image2_path):
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)
    
    if img1 is None or img2 is None:
        print("Error loading images!")
        return
    
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(img1_gray, img2_gray)
    change_percentage = np.sum(diff) / (diff.size * 255) * 100

    print(f"Growth Change Detected: {change_percentage:.2f}%")
    return change_percentage

if __name__ == "__main__":
    compare_images("datasets/sample_images/day1.jpg", "datasets/sample_images/day10.jpg")
