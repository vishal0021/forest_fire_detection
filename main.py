import cv2
import numpy as np


#img = cv2.imread('ColorCircles.png')
#img = cv2.imread('Cyclone 2.jpg')

img = cv2.imread('forest fire 3.jpg')

img_copy = img.copy()

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = [0, 47, 227]
upper = [104, 255, 255]
lower = np.array(lower, dtype="uint8")
upper = np.array(upper, dtype="uint8")

mask = cv2.inRange(hsv, lower, upper)
 
output = cv2.bitwise_and(img, hsv, mask=mask)
    
no_red = cv2.countNonZero(mask)

# Changing the colour-space
LUV = cv2.cvtColor(output, cv2.COLOR_BGR2LUV)
# Find edges
edges = cv2.Canny(LUV, 100, 400)
# Find Contours
contours, hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# Find Number of contours
print("Number of Contours is: " + str(len(contours)))
# Draw border around contours
cv2.drawContours(image=img, contours=contours, contourIdx=-1, color=(0, 0, 255), thickness=1, lineType=cv2.LINE_AA)

# Show the image with contours
#cv2.imshow('Contours', img)
#cv2.imwrite("ForestFireDetection.png", img)

###############################################################################################
hsv = cv2.cvtColor(img_copy, cv2.COLOR_BGR2HSV)

lower = [94, 0, 94]
upper = [160, 255, 255]
lower = np.array(lower, dtype="uint8")
upper = np.array(upper, dtype="uint8")

mask = cv2.inRange(hsv, lower, upper)
 
output = cv2.bitwise_and(img_copy, hsv, mask=mask)
    
no_red = cv2.countNonZero(mask)

# Changing the colour-space
LUV = cv2.cvtColor(output, cv2.COLOR_BGR2LUV)
# Find edges
edges = cv2.Canny(LUV, 200, 400)
# Find Contours
contours, hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# Find Number of contours
#print("Number of Contours is: " + str(len(contours)))
# Draw border around contours
cv2.drawContours(image=img, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=1, lineType=cv2.LINE_AA)

# Show the image with contours
cv2.imshow('Smoke & Fire', img)
#cv2.imwrite("ForestFireDetection.png", img)
#cv2.imwrite("Smoke_Fire.png", img)
###############################################################################################

#cv2.imshow("output", output)
#cv2.imshow('mask', mask)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
