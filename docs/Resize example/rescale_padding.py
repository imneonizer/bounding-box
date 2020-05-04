import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import imbo
import cv2

image = cv2.imread("car.jpg")
car = (88,50,827,591)
license_plate = (337, 499, 598, 561)

coordinates = [car, license_plate]
image, coordinates = imbo.rescale(image, coordinates, width=900, height=600, padding='replicate')

#car
x1,y1,x2,y2 = coordinates[0]
image = imbo.draw(image, x1, y1, x2, y2, "Blue car", rescale=True, bbox_color="blue", font_name="Kaushan")

#license place
x1,y1,x2,y2 = coordinates[1]
image = imbo.draw(image, x1, y1, x2, y2, "TS08FL8537", rescale=True, bbox_color="yellow", font_name="Typewriter")

cv2.imshow("img", imbo.resize(image, width=800))
cv2.imwrite("rescaled.jpg", image)
cv2.waitKey(0)
