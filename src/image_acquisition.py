# This file captures images from a camera or drone


import cv2

def capture_image(save_path="datasets/sample_images/crop_image.jpg"):
    camera = cv2.VideoCapture(0)  # 0 for default webcam
    ret, frame = camera.read()
    
    if ret:
        cv2.imwrite(save_path, frame)
        print(f"Image saved at {save_path}")
    else:
        print("Failed to capture image")
    
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_image()
