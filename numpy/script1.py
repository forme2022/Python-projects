import cv2

print("OpenCV version:")
print(cv2.__version__)

img=cv2.imread("galaxy.jpg",0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)


resized_img= cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("galaxy",resized_img)

cv2.imwrite("new galaxy.jpg",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()