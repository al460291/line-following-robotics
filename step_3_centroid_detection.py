"""Step 3 — Find the centroid of the detected red line."""
import cv2
import HAL
import WebGUI

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
        if moments["m00"] != 0:
            cx = moments["m10"] / moments["m00"]
            cy = moments["m01"] / moments["m00"]
            print("Line centroid: x={:.1f}, y={:.1f}".format(cx, cy))
        else:
            print("Contour has zero area")
    else:
        print("No red line detected")

    WebGUI.showImage(red_mask)
