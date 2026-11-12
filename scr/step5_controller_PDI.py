
import HAL
import WebGUI
import Frequency
import cv2
import numpy as np
import time

# ===== CONFIGURACION PID =====

KP = 1.5
KI = 0.03
KD = 0.08

VELOCIDAD_MAX = 5.0
VELOCIDAD_MIN = 2.0
GIRO_MAX = 2.5

# Variables del PID
error_anterior = 0.0
integral = 0.0
tiempo_anterior = time.monotonic()

while True:
    Frequency.tick(20)

    # 1. Obtener imagen de la camara
    imagen = HAL.getImage()

    if imagen is None or imagen.size == 0:
        HAL.setV(0)
        HAL.setW(0)
        integral = 0.0
        error_anterior = 0.0
        tiempo_anterior = time.monotonic()
        continue

    # 2. Convertir imagen a HSV
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

    # 3. Detectar linea roja
    rojo1 = cv2.inRange(
        hsv, np.array([0, 90, 60]),
        np.array([10, 255, 255])
    )

    rojo2 = cv2.inRange(
        hsv, np.array([170, 90, 60]),
        np.array([179, 255, 255])
    )

    mascara = rojo1 | rojo2

    alto, ancho = mascara.shape

    # 4. Seleccionar zona de la carretera
    y1 = int(alto * 0.55)
    y2 = int(alto * 0.85)
    zona = mascara[y1:y2, :]

    momentos = cv2.moments(zona)

    if momentos["m00"] > 0:

        # 5. Calcular posicion de la linea
        centro_linea = momentos["m10"] / momentos["m00"]
        centro_imagen = ancho / 2

        # Error normalizado [-1, 1]
        error = (centro_linea - centro_imagen) / centro_imagen

        # 6. Calcular tiempo transcurrido
        ahora = time.monotonic()
        dt = max(ahora - tiempo_anterior, 0.001)
        tiempo_anterior = ahora

        # ===== CONTROL PID =====

        # Proporcional
        P = KP * error

        # Integral (con anti-windup)
        integral += error * dt
        integral = np.clip(integral, -2.0, 2.0)
        I = KI * integral

        # Derivativo
        derivada = (error - error_anterior) / dt
        D = KD * derivada

        # Salida PID
        control = P + I + D

        # Giro del carrito
        giro = -control
        giro = np.clip(giro, -GIRO_MAX, GIRO_MAX)

        # 7. Adaptar velocidad en curvas
        velocidad = VELOCIDAD_MAX - 3.0 * abs(error)
        velocidad = np.clip(
            velocidad, VELOCIDAD_MIN, VELOCIDAD_MAX
        )

        # 8. Aplicar movimiento
        HAL.setV(float(velocidad))
        HAL.setW(float(giro))

        error_anterior = error

        # 9. Mostrar deteccion visual
        cv2.circle(
            imagen,
            (int(centro_linea), (y1 + y2) // 2),
            8, (0, 255, 0), -1
        )

        cv2.line(
            imagen,
            (int(centro_imagen), y1),
            (int(centro_imagen), y2),
            (255, 0, 0), 2
        )

    else:
        # Si pierde la linea, detener
        HAL.setV(0)
        HAL.setW(0)
        integral = 0.0
        error_anterior = 0.0
        tiempo_anterior = time.monotonic()

    # Mostrar imagen procesada
    WebGUI.showImage(imagen)
