import cv2
img1 = cv2.imread("f:\\Data\\avengers.jpg")
print(img1)
cv2.imshow("original",img1)
cv2.waitKey()
cv2.destroyAllWindows()