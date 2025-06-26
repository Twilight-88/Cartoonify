import cv2
from cartoonify import cartoonify_image

image_path = "../static/uploads/test1.jpg"
output_path = "../static/results/cartoon_sample1.jpg"

cartoon = cartoonify_image(image_path)
cv2.imwrite(output_path, cartoon)

print("Cartoonified image saved to:", output_path)
