"""Step 4 — Baseline P controller, adapted from the exercise slides.

Use inside the Unibotics Follow Line code editor (not standalone Python).
KP and forward speed are starting values to tune, not measured optima.
"""
import cv2
import HAL
import WebGUI

KP = 0.01
FORWARD_SPEED = 1.0

while True:
    image = HAL.getImage()
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    red_mask = cv2.inRange(hsv, (0, 125, 125), (30, 255, 255))

    contours, _ = cv2.findContours(
        red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    if contours:
        largest = max(contours, key=cv2.contourArea)
        moments = cv2.moments(largest)
        if moments["m00"] > 0:
            cx = moments["m10"] / moments["m00"]
            image_center = image.shape[1] / 2.0
            error = image_center - cx
            HAL.setV(FORWARD_SPEED)
            HAL.setW(KP * error)
        else:
            HAL.setV(0.0)
            HAL.setW(0.0)
    else:
        # Safety fallback: avoid continuing blindly when the line is lost.
        HAL.setV(0.0)
        HAL.setW(0.0)

    WebGUI.showImage(red_mask)
