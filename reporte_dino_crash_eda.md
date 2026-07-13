# Reporte EDA - Operación Dino Crash 
**Analista:** [Angel Gabriel Anguiano Mejía / 21121494]

## 1. Problema y dataset (Misión 1)
### P1 — Muerte en el siguiente frame
- Y: Binaria, porque es la más sencilla que nos dirá si vive o muere es decir, 0 aún vive, 1 ya estiró la pata
- X (mínimo 5 variables): velocidad (flotante porque la velocidad puede ir incrementado de manera natural, es decir lenta, a algo que se sienta de golpe como en una entero), distancia del siguiente obstáculo (entero), tipo de obstáculo (categórica), salto (binario, para saber si el usuario ejecutó o no un salto), tiempo (flotante, tiempo estimado de la partida), puntuación (entero, por cada obstáculo superado)
- Granularidad:Un frame del juego representa el estado actual del dinosaurio y del escenario en el instante específico de dicho frame 
- Tamaño mínimo de dataset:Al menos una cantidad significativa de datos o en este caso frames para que el modelo aprenda el comportamiento del jugador, las velocidades, los obstáculos. 


### P2 — Puntos alcanzados esta partida al morir
- Y: Entera, porque es la que nos dirá la cantidad de puntos alcanzados por el usuario antes de perder la partida
- X (mínimo 5 variables): velocidad final (flotante porque nos indica la velocidad que el usuario no pudo superar), tipo de obstáculo final (categórica, porque nos dirá que objeto es el más complicado para el usuario superar), saltos (entero, la cantidad de saltos que realizó el usuario antes de morir), tiempo final (flotante, el tiempo que tardó el usuario en perder), puntuación final (entero, la puntuación final del usuario)
- Granularidad:Una partida completa, ya que al final de esta conoceríamos todos los datos finales del usuario.
- Tamaño mínimo de dataset:Al menos una cantidad significativa de partidas para observar los diferentes tipos de habilidades de diferentes usuarios o de uno mismo (para evaluar si hay una mejora entre partidas), las velocidades, aparición de obstáculos y las puntuaciones finales 


### P3 — Próximo obstáculo 
- Y: categórica, ya que el siguiente obstáculo en venir puede ser diferente al anterior o igual
- X (mínimo 5 variables):velocidad(numérica, ya que nos indica qué tan rápido va el juego y dependiendo de esto pueden aparecer más obstáculos o ciertos obstáculos con las frecuencia), tiempo (numérica, nos indica cuánto tiempo ha pasado en el juego y la dificultad a cambiar o como cambiar la dificultad), puntuación (numérica, porque nos indica cuál es la facilidad del usuario de traspasar esos obstáculos), tipo de obstáculo(dependiendo de la velocidad del juego y de la habilidad del jugador los obstáculos tendrán que ser cada vez más aleatorios), salto(entero, es la cantidad de saltos que ha dado el usuario antes de llegar al siguiente obstáculo)
- Granularidad: Un frame del juego, ya que en dicho frame puede o no aparecer un nuevo tipo de obstáculo
- Tamaño mínimo de dataset: Una cantidad significativas de frames para que cada que aparece un tipo de obstáculo y no solo se base en unos pocos


## 2. Diccionario y muestra (Misión 2)
- Patrón en died=1:
En las filas donde el jugador murió observamos que la distancia al objeto donde colisionó es muy corta y el jugador no alcanzó a saltar a tiempo.
- ¿Falta alguna columna?
Algunas de las columnas que hagan falta serían la altura del dinosaurio, si este se encontraba agachado al momento que el jugador colisionó, la acción que realizó si en lugar de saltar se agachó, ya que esto puede llegar a influir en que el dinosaurio estirara la pata 

## 3. Checklist EDA (Misión 3)
-¿La clase objetivo está balanceada?
No, la mayor parte de los frames corresponden a que el señor dinosaurio sigue con vida y solamente unos pocos representan que estiró la pata, por lo que está desbalanceado.

-¿Hay variables correlacionales?
Sí, la puntuación y el tiempo están relacionados, ya que mientras más tiempo dura la partida, mayor será la puntuación del usuario

-¿Hay outliers?
Podrían existir ciertos valores no comunes, como distancias negativas al obstáculo que indica qué tan cerca está el usuario de colisionar o velocidades fuera del rango normal del juego, estos datos deberían de revisarse antes de poder siquiera entrenar al modelo.

-Leakage
Por ejemplo utilizar el score final de la partida para predecir si el dinosaurio morirá en el siguiente frame

-i.i.d
No sería correcto mezclar frames de una misma partida entre entrenamiento y la prueba, porque son muy parecidas, el modelo podría aprender de una partida en lugar de varios comportamientos

## 4. Interpretación de resúmenes (Misión 4)
-Desbalance:
Sí, debido a que el dataset tiene aproximadamente entre 10,000 frames a 12,000 frames y solamente 50 corresponden a una muerte, y la clase muerte solo representa una muy pequeña parte de las muertes para el dataset

-Implica para la métrica:
En este caso no sería recomendable utilizar únicamente accuracy, porque un modelo podría acertar casi siempre diciendo que el dinosaurio no muere, sería mejor utilizar otro tipo de métricas.

-Dist_obstacle es útil:
En este caso sí, en el resumen se menciona que la gran parte de las veces que el dinosaurio estiró la pata sucede cuando la distancia al obstáculo es menor a 20, es una variable importante para predecir.

-¿Qué sugiere la distribución de la puntuación?:
La puntuación tiene una cola larga hacia la derecha, por lo que probablemente no siga una distribución lineal, sería conveniente analizarlo antes de decidir qué modelo usar


## 5. Elección de modelo (Misiones 5–6)
| Escenario | Tras tu EDA, ¿qué fila aplica? | Modelo que propondrías | 2 condiciones del dataset que deben cumplirse |
|------------|--------------------------------|-------------------------|------------------------------------------------|
| P1 | Y binaria, tabular | Regresión logística o Árbol de decisión | Tener suficientes ejemplos de muerte y datos completos. |
| P2 | Y numérica | Regresión lineal o Árbol regresor | Tener suficientes partidas y una relación clara entre las variables y la puntuación. |
| P3 | Y categórica multiclase | Árbol de decisión o Regresión logística multinomial | Tener ejemplos de todos los tipos de obstáculos y variables suficientes para diferenciarlos. |

-Contra ejemplo I:
Un árbol muy profundo no sería recomendable si el dataset es peque podría aprender únicamente esos datos y no generalizar correctamente

-Contra ejemplo II:
Una red neuronal tendría sentido si existieran múltiples partidas y suficientes ejemplos de todos los tipos de obstáculos para que pudiera aprender patrones más completos, también una buena idea sería que aprenda de diferentes jugadores 

-¿Se podría resolver P1 con reglas?:
Sí, por ejemplo usando una regla como si la distancia al obstáculo es muy pequeña y el dinosaurio no está saltando, entonces estira la pata

## Síntesis (5 líneas)
¿Qué dataset pedirías primero y qué modelo *solo después* del EDA?
Primero solicitaría un dataset con suficientes partidas y variables que describen correctamente el estado del dinosaurio y del escenario, después realizaría un EDA para verificar la calidad de los datos, el balance de las clases y los posibles problemas como data leakage, con base a esos resultados elegiría el modelo más adecuado, de esta manera el modelo se selecciona según los datos disponibles y no únicamente por su popularidad.