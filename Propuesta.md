#   Propuesta para codificar el proyecto

##  Descripción general

Se me ocurre repartir el código en 2 grupos principales, el de obtención de datos y el generador de gráficas.

El de obtención de datos se puede separar por distintas librerías[^1], cada una con una función específica. Y el de generar las gráficas sería bastante simple, podríamos incluso generar GIFs animados si almacenamos todos los datos y no solo los iniciales y finales.

[^1]: En Python podemos hacer "librerías", que contendrían las funciones haciendo distintos archivos ```.py``` y luego incluyéndolas en el main.

***

##  Definiciones

###  Hoja de datos

Para llevar el registro de las posiciones, velocidades y demás datos, se me ocurre usar el archivo CSV e ir agregando por bloques separados por un enter (un solo enter es importante para poder usar el comando ```every``` en gnuplot después).

Un ejemplo de la hoja de datos sería:

```
ID, m, q, radius, rx, ry, rz, vx, vy, ax, ay

0, 1, 1, 1, 5.96, 1.14, 1.15, 1.33, 1.03, 1.09, 1.16
1, 1, 1, 1, 1.10, 3.72, 9.35, 2.65, 1.29, 1.37, 1.27
2, 1, 1, 1, 2.96, 1.94, 7.29, 1.69, 1.45, 4.02, 1.07
3, 1, 1, 1, 3.00, 7.60, 4.50, 8.12, 9.68, 8.34, 5.92
4, 1, 1, 1, 7.71, 2.21, 3.50, 1.21, 4.24, 3.20, 2.11

0, 1, 1, 1, 1.38, 2.36, 3.62, 8.85, 3.98, 5.94, 3.51
1, 1, 1, 1, 2.20, 5.46, 8.32, 5.75, 1.15, 5.12, 3.40
2, 1, 1, 1, 1.65, 1.15, 1.32, 2.72, 3.47, 9.94, 2.22
3, 1, 1, 1, 6.11, 2.97, 1.33, 2.30, 2.85, 1.84, 3.66
4, 1, 1, 1, 2.22, 1.11, 7.10, 6.74, 1.08, 5.43, 1.24

0, 1, 1, 1, 3.00, 4.29, 1.57, 1.54, 2.99, 3.30, 5.00
1, 1, 1, 1, 1.97, 9.82, 1.36, 4.17, 1.27, 1.39, 4.01
2, 1, 1, 1, 1.18, 4.76, 4.39, 6.06, 3.96, 9.64, 4.88
3, 1, 1, 1, 1.30, 6.54, 8.35, 5.99, 6.98, 9.37, 5.28
4, 1, 1, 1, 2.13, 1.08, 3.30, 1.47, 9.97, 8.77, 1.73
```

La primera línea podrá parecer mala idea, pero es sencilla de ignorar tanto en gnuplot como en python.

Como sugerencia, para leer la hoja de datos en las distintas funciones, simplemente leer las últimas ```n``` líneas, con ```n``` la cantidad de partículas en juego, el orden en el que se lean no es importante porque en los datos está el ID.

###  Hoja de parámetros
Una hoja sencilla para colocar los parámetros de la simulación. Un ejemplo de esta sería:

```
Case: HighAPF
Particles: 10
Mass: 1
Charge: 1
Radius: 1
BoxX: 20
BoxY: 20
```

***

##  Obtención de datos

Mi propuesta es separar este en las siguientes librerías:

*   Condiciones iniciales
*   Ecuación de movimiento
*   Interacción de nuevas posiciones
*   Conservación del momento
*   Main

### Condiciones iniciales
Esta librería debería separarse en dos funciones, una que asigne valores aleatorios a los puntos iniciales para utilizar cuando el factor de empaquetamiento es pequeño, y otra que comience con las posiciones ideales y quite una cantidad de puntos deseada. Además las funciones deben de encargarse de crear la hoja de datos ```particles.dat``` y escribir el primer bloque de datos en esta.

### Ecuación de movimiento
Esta librería debería tener una función que dado el bloque de datos del intervalo de tiempo actual, calcule la fuerza sobre cada partícula, y con esto calcule las posiciones y velocidades para el siguiente intervalo. Finalmente, que añada un bloque con estos datos a la hoja de datos.

A esta función no le debe importar si hay o si no hay un choque entre partículas o con alguna pared, de eso se encargará la siguiente librería.

### Interacción de nuevas posiciones
Esta librería se encargará de descartar los casos en los que las partículas se superpongan o traspasen las paredes. Leerá el último bloque de la hoja de datos, comparando partícula por partícula, en el caso de un choque, debe hacer los ajustes necesarios, moviendo las partículas y ajustando las velocidades corriendo la librería de conservación de momento. 

### Conservación del momento
Para esta librería es muy importante acordar la sintaxis que se utilizará, ya que no modificará datos de la hoja de datos, sino que debe retornar los valores de las velocidades para que la librería de interacción de nuevas partículas se encargue de colocarlos en la hoja de datos. Deben hacerse dos funciones, una para cuando el choque sea entre dos partículas, y otra para cuando el choque sea entre dos paredes.

### Main
Función principal que va a ejecutar en orden las funciones anteriores. Se encargará de leer la hoja de parámetros para asignar los valores adecuados en las funciones.

*** 

##  Generador de gráficas
Este sería un código sencillo de gnuplot que plotee los puntos utilizando círculos con el radio deseado, además un vector de velocidad centrado en este. Utilizando una terminal gif se pueden animar los plots utilizando un ```for``` para repetir el mismo código para los distintos bloques de datos.