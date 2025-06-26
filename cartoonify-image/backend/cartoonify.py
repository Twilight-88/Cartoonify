import cv2
import numpy as np

def cartoonify_image(image_path):
    img = cv2.imread(image_path)

    if img is None:
        raise ValueError("Image not found or invalid image format.")

    # 1. Resize
    img = cv2.resize(img, (640, 480))

    # 2. Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Apply median blur
    gray_blur = cv2.medianBlur(gray, 5)

    # 4. Detect edges
    edges = cv2.adaptiveThreshold(gray_blur, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)

    # 5. Apply bilateral filter
    color = cv2.bilateralFilter(img, d=9, sigmaColor=300, sigmaSpace=300)

    # 6. Combine color and edges
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon
