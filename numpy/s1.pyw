import cv2

img=cv2.imread("galaxy.jpg",0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)


cv2.imshow("galaxy",img)
cv2.waitKey(0)
cv2.destroyAllWindows