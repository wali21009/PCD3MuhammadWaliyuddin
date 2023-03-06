import cv2
import numpy as np

#load picture
img = cv2.imread('image/lofi.jpeg')
kernel_size = 5
kernel = np.ones((kernel_size,kernel_size),np.float32)/(kernel_size*kernel_size)
filtered_img = cv2.filter2D(img,-1,kernel)

# result
cv2.imshow('Filtered Image', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()