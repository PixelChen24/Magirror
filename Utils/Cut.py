from cv2 import cv2 as cv
img=cv.imread("../Background/1080p.png")
Newimg=img[:450,:580,:]
cv.imwrite("../CutBackground.png",Newimg)