import numpy
import cv2

#importing photos , please use your image 
a=cv2.imread("1.PNG")
b=cv2.imread("2.png")

#checking shape of first image
a.shape

#checking shape of second image
b.shape

#using slicing operation to match the rows and column , change the values according to your picture
a=a[:285,:579]

a.shape

# using concatenate() to make a collage
z=numpy.concatenate((a,b),axis=1)
y=numpy.concatenate((a,b),axis=0)

#viewing the collage made
cv2.imshow("vertical_stacking",y)
cv2.imshow("horizontal_stacking",z)
cv2.waitKey()
cv2.destroyAllWindows()

