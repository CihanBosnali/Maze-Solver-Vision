import cv2
import numpy as np 

def find_entrance_by_color(image, lower_color=np.array([0,100,0]), upper_color=np.array([1,255,1])):
    mask = cv2.inRange(image, lower_color, upper_color)
    return mask

    
def main():
    image = cv2.imread("maze.png")

    mask_entrance = find_entrance_by_color(image)
    mask_exit = find_entrance_by_color(image, lower_color=np.array([0,0,100]), upper_color=np.array([1,1,255]))

    while True:
        cv2.imshow("Green", mask_entrance)
        cv2.imshow("Red", mask_exit)

        if cv2.waitKey() == 27:
            break

main()
