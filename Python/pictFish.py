import cv2
import numpy as np

img = cv2.imread("D:\work\IVT-27D\MatveevaMarinaVlad1\Student\Opencv_first\picture.jpg",0)
cv2.imshow("image",img)
print(img)

f = open('image.txt','w')

st_ = ""

for i in range(173):
    for j in range(200):
        st_+=str(img[i][j])+" "
f.write(st_)
f.close


cv2.waitKey(0)



cv2.destroyAllWindows()
