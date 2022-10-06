import cv2
import glob

images=glob.glob("*.jpg")

for sooo in images:
    imgg=cv2.imread(sooo,0)
    re1=cv2.resize(imgg,(100,100))
    cv2.imshow("heyyyy",re1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+sooo,re1)
    
