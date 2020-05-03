import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
import cv2
import imbo

image = cv2.imread("high_resolution.jpg")
orig_image_copy1 = image.copy()
orig_image_copy2 = image.copy()

left = 4898
top = 1674
right = 6998
bottom = 2822
label = "Taxi cab"
bbox_color = "white"
label_color = "white-contrast"

#without rescale=False
image = imbo.draw(orig_image_copy1, left, top, right, bottom, label, bbox_color=bbox_color,
                  rescale=False, label_color=label_color, font_size=30, thickness=3, adjust_label=(-1, 0))
cv2.imwrite("without_rescaling.jpg", image)


#with rescale=True
image = imbo.draw(orig_image_copy2, left, top, right, bottom, label, bbox_color=bbox_color,
                  rescale=True, label_color=label_color, font_size=30, thickness=3, adjust_label=(-1, 0))
cv2.imwrite("with_rescaling.jpg", image)
