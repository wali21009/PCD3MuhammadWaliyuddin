import cv2

# load 2 image
img1 = cv2.imread('image/resize1.jpg')
img2 = cv2.imread('image/resize2.jpg')

# same size image
if img1.shape != img2.shape:
    print('different size image')
else:
    #result
    result = cv2.subtract(img1, img2)
    cv2.imshow('Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
