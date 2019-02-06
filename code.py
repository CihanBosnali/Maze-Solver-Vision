import cv2
import numpy as np

# Import the image
img = cv2.imread('maze.png')

width = len(img[0,:])
height = len(img[:,0])

# Define color for green
Bg = 0
Gg = 150
Rg = 0

result_xg = []
result_yg = []
for i in range(height):
    for j in range(width):
        for k in range(2):
            if (img[i,j,0]==Bg and img[i,j,1]>=Gg and img[i,j,2]==Rg):

                result_xg.append(j)
                result_yg.append(i)
                print("a")

for i in range(height):
    for j in range(width):
        for k in range(2):
            if (img[i,j,0]==Br and img[i,j,1]==Gr and img[i,j,2]>=Rr):
                result_xr.append(j)
                result_yr.append(i)
                print("a")

# Define color for red
Br = 0
Gr = 0
Rr = 150

result_xr = []
result_yr = []

while True:
    cv2.imshow("img", img)

    #_, cont, a = cv2.findContours(img, cv2.MORPH_OPEN, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(img, cont, -1, (0,225,0), 3)

    for x1 in tuple(result_xg):
        for y1 in tuple(result_yg):
            for x2 in tuple(result_xr):
                for y2 in tuple(result_yr):
                    cv2.line(img, (x1, x1), (y1, y1), (0,255,0))
                    cv2.line(img, (x2, x2), (y2, y2), (0,255,0))
                    print("a")

    Key = cv2.waitKey()
    if Key == 27:
        break