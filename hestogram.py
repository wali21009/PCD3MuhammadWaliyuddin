import cv2
import matplotlib.pyplot as plt

# Load Picture
img = cv2.imread('image/Home.jpg', 0)

# calculate histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)

# Show result
plt.show()