import cv2
import numpy as np 


def main():
    image = cv2.imread("maze.png")

    lower_green = np.array([0,100,0])
    upper_green = np.array([1,255,1])

    lower_red = np.array([0,0,100])
    upper_red = np.array([1,1,255])

    mask_green = cv2.inRange(image, lower_green, upper_green)
    mask_red = cv2.inRange(image, lower_red, upper_red)

    while True:
        cv2.imshow("Green", mask_green)
        cv2.imshow("Red", mask_red)

        if cv2.waitKey() == 27:
            break

main()