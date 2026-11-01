"""Step 2 — Detect the red line, using the HSV range in the slides."""
import cv2
import HAL
import WebGUI

while True:
    image = HAL.getImage()
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    red_mask = cv2.inRange(hsv, (0, 125, 125), (30, 255, 255))
    WebGUI.showImage(red_mask)
