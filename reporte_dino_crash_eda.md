# Reporte EDA - Operación Dino Crash 
**Analista:** [Angel Gabriel Anguiano Mejia / 21121494]

## 1. Problema y dataset (Misión 1)
### P1 — Muerte en el siguiente frame
- Y: Binaria, porque es la mas sencilla que nos dirá si vive o muere es decir, 0 aún vive, 1 ya estiro la pata
- X (mínimo 5 variables): velocidad (flotante porque la velocidad puede ir incrementado de manera natural, es decir lenta, a algo que se sienta de golpe como en una entero), distancia del siguiente obstaculo (entero), tipo de obstaculo (categorica), salto (binario, para saber si el usuario ejecuto o no un salto), tiempo (flotante, tiempo estimado de la partida), puntuacion (entero, por cada obstaculo superado)
- Granularidad:Un frame del juego representa el estado actual del dinosaurio y del escenario en el instante especifico de dicho frame 
- Tamaño mínimo de dataset:Al menos una cantidad significativa de datos o en este caso frames para que el modelo aprenda el comportamiento del jugador, las velocidades, los obstaculos. 


### P2 — Puntos alcanzados esta partida al morir
- Y: Entera, porque es la que nos dira la cantidad de puntos alcanzados por el usuario antes de perder la partida
- X (mínimo 5 variables): velocidad final (flotante porque nos indica la velocidad que el usuario no pudo superar), tipo de obstaculo final (categorica, porque nos dira que objeto es el mas complicado para el usuario superar), saltos (entero, la cantidad de saltos que realizo el usuario antes de morir), tiempo final (flotante, el tiempo que tardo el usuario en perder), puntuacion final (entero, la puntuación final del usuario)
- Granularidad:Una partida completa, ya que al final de esta conoceriamos todos los datos finales del usuario.
- Tamaño mínimo de dataset:Al menos una cantidad significativa de partidas para observar los diferentes tipos de habilidades de diferentes usuarios o de uno mismo (para evaluar si hay una mejora entre partidas), las velocidades, aparicion de obstaculos y las puntuaciones finales 


### P3 — Proximo obstaculo 
- Y: categorica, ya que el siguiente obstaculo en venir puede ser diferente al anterior o igual
- X (mínimo 5 variables):
- Granularidad: Un frame del juego, ya que en dicho frame puede o no aparecer un nuevo tipo de obstáculo
- Tamaño mínimo de dataset: Una cantidad signifi
## 2. Diccionario y muestra (Misión 2)
- Patrón en died=1:
- ¿Falta alguna columna?

## 3. Checklist EDA (Misión 3)
(respuestas a 3 preguntas + leakage + i.i.d.)

## 4. Interpretación de resúmenes (Misión 4)
(desbalance, métricas, dist_obstacle)

## 5. Elección de modelo (Misiones 5–6)
(tabla P1/P2/P3 + contraejemplos)

## Síntesis (5 líneas)
¿Qué dataset pedirías primero y qué modelo *solo después* del EDA?