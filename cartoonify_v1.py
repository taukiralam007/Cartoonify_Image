import cv2

# Load the image
img = cv2.imread("C:\\Users\\admin\\Desktop\\flower.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply median blur to reduce noise
gray = cv2.medianBlur(gray, 5)

# Apply bilateral filter for cartoonification effect
bilateral = cv2.bilateralFilter(img, 9, 100, 100)

# Create the output image by combining the grayscale and bilateral filtered images
cartoon = cv2.bitwise_and(bilateral, bilateral, mask=gray)

# Display the output image
cv2.imshow("Cartoonized Image", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
