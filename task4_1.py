import cv2

import numpy 

image = numpy.ones((600,600,3))

center_coordinates=(300,300)
radius=290
color = (0, 0, 0)
thickness=40
image = cv2.circle(image, center_coordinates, radius, color, thickness)

center_coordinates=(300,300)
radius=250
color = (255, 255, 255)
thickness=20
image = cv2.circle(image, center_coordinates, radius, color, thickness)

center_coordinates=(300,300)
radius=210
color = (0, 0, 0)
thickness=40
image = cv2.circle(image, center_coordinates, radius, color, thickness)

center_coordinates=(300,300)
radius=170
color = (255, 255, 255)
thickness=20
image = cv2.circle(image, center_coordinates, radius, color, thickness)

center_coordinates=(300,300)
radius=130
color = (0, 0, 0)
thickness=40
image = cv2.circle(image, center_coordinates, radius, color, thickness)

center_coordinates=(300,300)
radius=90
color = (255, 255, 255)
thickness=20
image = cv2.circle(image, center_coordinates, radius, color, thickness)

center_coordinates=(300,300)
radius=50
color = (0, 0, 0)
thickness=40
image = cv2.circle(image, center_coordinates, radius, color, thickness)

cv2.imshow('myjpg',image)
cv2.waitKey()
cv2.destroyAllWindows()

