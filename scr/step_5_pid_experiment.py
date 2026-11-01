"""Optional experiment — tune P, PD, or PID control in the simulator.

The gains below START as P control (KI=KD=0). To evaluate PD/PID,
change KI and/or KD, then record results. Values are NOT validated.
The derivative/integral use discrete time steps (not physical seconds).
"""
import cv2
import HAL
import WebGUI

KP = 0.01
KI = 0.0
KD = 0.0
FORWARD_SPEED = 1.0
INTEGRAL_LIMIT = 1000.0

previous_error = 0.0
integral_error = 0.0

while True:
    image = HAL.getImage()
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    red_mask = cv2.inRange(hsv, (0, 125, 125), (30, 255, 255))

    contours, _ = cv2.findContours(
        red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    detected = False
    if contours:
        largest = max(contours, key=cv2.contourArea)
        moments = cv2.moments(largest)
        if moments["m00"] > 0:
            detected = True
            cx = moments["m10"] / moments["m00"]
            error = (image.shape[1] / 2.0) - cx
            integral_error += error
            integral_error = max(-INTEGRAL_LIMIT, min(INTEGRAL_LIMIT, integral_error))
            derivative_error = error - previous_error
            steering = KP * error + KI * integral_error + KD * derivative_error
            HAL.setV(FORWARD_SPEED)
            HAL.setW(steering)
            previous_error = error

    if not detected:
        HAL.setV(0.0)
        HAL.setW(0.0)
        integral_error = 0.0
        previous_error = 0.0

    WebGUI.showImage(red_mask)
