import cv2
import numpy as np 

def get_image(image_path):
    # TODO: Get image from camera
    return cv2.imread(image_path)

def find_endpoints_by_color(image, lower_color=np.array([0,100,0]), upper_color=np.array([20,255,20])):
    mask = cv2.inRange(image, lower_color, upper_color)
    _, contours, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    x,y,w,h = cv2.boundingRect(contours[0])
    center = (int(x+(w/2)), int(y+(h/2)))

    return center

def main():
    image = get_image("maze.png")

    entrance_location = find_endpoints_by_color(image)
    exit_location = find_endpoints_by_color(image, lower_color=np.array([0,0,100]), upper_color=np.array([20,20,255]))

    cv2.line(image, entrance_location, exit_location, (255,0,255), 3)

    cv2.imshow("img", image)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
