
import HAL
import WebGUI
import Frequency
import cv2
import numpy as np
import time

KP = 1.5
KD = 0.08

VELOCIDAD_MAX = 3.0
VELOCIDAD_MIN = 1.5
GIRO_MAX = 2.5

error_anterior = 0.0
tiempo_anterior = time.monotonic()

while True:
    Frequency.tick()

    imagen = HAL.getImage()

    if imagen is None or imagen.size == 0:
        HAL.setV(0)
        HAL.setW(0)
        error_anterior = 0.0
        tiempo_anterior = time.monotonic()
        continue

    alto, ancho = imagen.shape[:2]

    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

    rojo1 = cv2.inRange(
        hsv, np.array([0, 90, 60]),
        np.array([10, 255, 255])
    )
    rojo2 = cv2.inRange(
        hsv, np.array([170, 90, 60]),
        np.array([179, 255, 255])
    )

    mascara = rojo1 | rojo2

    y1 = int(alto * 0.55)
    y2 = int(alto * 0.85)

    zona = mascara[y1:y2, :]
    momentos = cv2.moments(zona)

    if momentos["m00"] > 0:

        centro_linea = momentos["m10"] / momentos["m00"]
        centro_imagen = ancho / 2

        error = (centro_linea - centro_imagen) / centro_imagen

        ahora = time.monotonic()
        dt = max(ahora - tiempo_anterior, 0.001)
        tiempo_anterior = ahora

        # CONTROLADOR PD
        P = KP * error

        derivada = (error - error_anterior) / dt
        D = KD * derivada

        control = P + D

        giro = np.clip(-control, -GIRO_MAX, GIRO_MAX)

        velocidad = np.clip(
            VELOCIDAD_MAX - 3 * abs(error),
            VELOCIDAD_MIN,
            VELOCIDAD_MAX
        )

        HAL.setV(float(velocidad))
        HAL.setW(float(giro))

        error_anterior = error

        cv2.circle(
            imagen,
            (int(centro_linea), (y1 + y2) // 2),
            8, (0, 255, 0), -1
        )

    else:
        HAL.setV(0)
        HAL.setW(0)
        error_anterior = 0.0
        tiempo_anterior = time.monotonic()

    WebGUI.showImage(imagen)
