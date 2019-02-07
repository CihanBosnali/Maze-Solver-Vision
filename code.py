import cv2
import numpy as np

# Import the image
img = cv2.imread('maze.png')

result_x = []
result_y = []

def pixel_find_red(B, G, R):
    width = len(img[0,:])
    height = len(img[:,0])
    for i in range(height):
        for j in range(width):
            for k in range(2):
                if (img[i,j,0]==B and img[i,j,1]==G and img[i,j,2]>=R):
                    result_x.append(j)
                    result_y.append(i)
                    print("a")

def pixel_find_green(B, G, R):
    width = len(img[0,:])
    height = len(img[:,0])
    for i in range(height):
        for j in range(width):
            for k in range(2):
                if (img[i,j,0]==B and img[i,j,1]>=G and img[i,j,2]==R):
                    result_x.append(j)
                    result_y.append(i)
                    print("c")


np.vectorize(pixel_find_green(0, 150, 0))
np.vectorize(pixel_find_red(0, 0, 150))

print(result_x)

def pixel_finding():
    x1 = max(str(result_x),key=lambda item:item[1])[0]
    y1 = max(str(result_y),key=lambda item:item[1])[0]
    cv2.line(img, (x1, x1), (y1, y1), (0,255,0))
    print("b")

#np.vectorize(pixel_finding())

pixel_finding()

while True:
    cv2.imshow("img", img)

    #_, cont, a = cv2.findContours(img, cv2.MORPH_OPEN, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(img, cont, -1, (0,225,0), 3)

    Key = cv2.waitKey()
    if Key == 27:
        break