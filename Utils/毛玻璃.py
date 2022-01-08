import cv2
import numpy as np
img = cv2.imread(r'C:\Users\mx\Desktop\111.png')
h,w,c=img.shape
for row in range(h):
    for col in range(w):
        srand=np.random.normal(0,30,3)
        b=img[row,col,0]
        g=img[row,col,1]
        r=img[row,col,2]
        if b+srand[0]>255:
            img[row,col,0]=255
        elif b+srand[0]<0:
            img[row,col,0]=0
        else: img[row,col,0]=b+srand[0]

        if g+srand[1]>255:
            img[row,col,1]=255
        elif g+srand[1]<0:
            img[row,col,1]=0
        else: img[row,col,1]=g+srand[1]
        if r+srand[2]>255:
            img[row,col,2]=255
        elif r+srand[2]<0: img[row,col,2]=0
        else: img[row,col,2]=r+srand[2]
        dst=cv2.blur(img,(2,24))
        dst=cv2.GaussianBlur(img,(0,0),20)
        cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
        cv2.imshow("Image", img)
        cv2.imshow("Gaussian", dst)
        cv2.waitKey (0)
        cv2.destroyAllWindows()