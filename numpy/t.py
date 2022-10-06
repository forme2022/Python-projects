import cv2
print("OpenCV version:")
print(cv2.__version__)

img = cv2.imread("galaxy.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("galaxy", img)
cv2.imshow("galaxy - gray", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()