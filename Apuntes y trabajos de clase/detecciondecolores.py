import cv2
import numpy as np

# Leer la imagen
img = cv2.imread('Sandrome.jpg')

# Convertir la imagen al espacio de color HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Definir el rango inferior y superior para detectar verde
lower_green = np.array([100, 60, 60])  # Hue, Saturación, Brillo mínimos
upper_green = np.array([130, 255, 255])  # Hue, Saturación, Brillo máximos

#lower_green1 = np.array([170, 60, 60])  # Hue, Saturación, Brillo mínimos
#upper_green1 = np.array([180, 255, 255])  # Hue, Saturación, Brillo máximos


# Crear una máscara que solo incluya los píxeles dentro del rango
mask = cv2.inRange(hsv, lower_green, upper_green)
#mask2 = cv2.inRange(hsv, lower_green1, upper_green1)

#mask = mask1+mask2

# Aplicar la máscara a la imagen original
result = cv2.bitwise_and(img, img, mask=mask)

# Mostrar la imagen original y la imagen con el color detectado
cv2.imshow("Imagen Original", img)
cv2.imshow("Color Detectado", result)
cv2.imshow("Mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()