from image_acquisition import capture_image
from disease_detection import predict_disease
from growth_analysis import compare_images
from soil_assessment import analyze_soil
from alerts import send_alert

def main():
    print("Starting Crop Monitoring System...\n")

    # Step 1: Capture Image
    image_path = "datasets/sample_images/crop_image.jpg"
    capture_image(image_path)

    # Step 2: Disease Detection
    disease_result = predict_disease(image_path)

    # Step 3: Growth Analysis (Example)
    growth_change = compare_images("datasets/sample_images/day1.jpg", "datasets/sample_images/day10.jpg")

    # Step 4: Soil Assessment
    soil_quality = analyze_soil("datasets/sample_images/soil.jpg")

    # Step 5: Send Alert if Problem Detected
    if disease_result != "Healthy" or growth_change > 10 or soil_quality < 50:
        send_alert("farmer@example.com", f"Alert: {disease_result} detected. Growth Change: {growth_change}%. Soil Quality: {soil_quality}%.")

if __name__ == "__main__":
    main()
